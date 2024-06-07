"""
parsing Uniswap v3 contract values

This class converts internal Uniswap v3 contract values into values that make sense
from a financial perspective, either in Wei or in token units. It also allows to
convert Uniswap v3 contract parameters into generic constant product curve parameters
that are suitable for our ``CPC`` class.

---
(c) Copyright Bprotocol foundation 2023-24.
All rights reserved.
Licensed under MIT.
"""
from dataclasses import dataclass

from arb_analyzer.interfaces.input import Token


@dataclass(frozen=True)
class Univ3Calculator():
    FEE80       = 80
    FEE100      = 100
    FEE250      = 250
    FEE450      = 450
    FEE500      = 500
    FEE2500     = 2500
    FEE3000     = 3000
    FEE10000    = 10000

    TICKSZ = {FEE80: 1, FEE100: 1, FEE250: 5, FEE450: 10, FEE500: 10, FEE2500: 50, FEE3000: 60, FEE10000: 200}

    Q96 = 2 ** 96
    Q192 = 2 ** 192
    
    tkn0: Token
    tkn1: Token
    sp96: int # sqrt_price_q96
    tick: int
    liquidity: int
    fee_const: int
    
    @classmethod
    def from_dict(cls, d, fee_const):
        """
        alternative constructor from a dictionary
        
        :d:             dict with keys: token0 [address], token1 [address], sqrt_price_q96, tick, liquidity
        :fee_const:     fee constant (FEE100, ...)
        :tkn0decv:      optional token0 decimals value (eg 6, 18)
        :tkn1decv:      optional token1 decimals value (eg 6, 18)
        :addrdec:       optional dictionary of token address to decimals (eg {"0x123...": 18})
        """
        return cls(
            tkn0 = d["token0"],
            tkn1 = d["token1"],
            sp96 = d["sqrt_price_q96"],
            tick = d["tick"],
            liquidity = d["liquidity"],
            fee_const = fee_const,
        )
    
    class DecimalsMissingError(Exception): pass
    
    def __post_init__(self):
        super().__setattr__('sp96', int(self.sp96)) 
        super().__setattr__('tick', int(self.tick)) 
        super().__setattr__('liquidity', int(self.liquidity)) 
        super().__setattr__('fee_const', int(self.fee_const)) 
        assert self.fee_const in {self.FEE80, self.FEE100, self.FEE250, self.FEE450, self.FEE500, self.FEE2500, self.FEE3000, self.FEE10000}, "fee not one of the FEEXXX constants {self.fee_const}"

    @property
    def pair(self):
        """the directed pair tknb/tknq = tkn0/tkn1"""
        return f"{self.tkn0.id}/{self.tkn1.id}"
    
    @property
    def fee(self):
        """fee in basis points"""
        return self.fee_const / 1000000
    
    @property
    def ticksize(self):
        """tick size"""
        return self.TICKSZ[self.fee_const]
    
    @property
    def tickab(self):
        """returns the tick values of Pa and Pb"""
        ticka = (self.tick // self.ticksize) * self.ticksize
        return ticka, ticka + self.ticksize
    
    @property
    def papb_raw(self):
        """raw Pa and Pb values (1.0001**tickab)"""
        ta, tb = self.tickab
        return (1.0001 ** ta, 1.0001 ** tb)
    
    @property
    def papb_tkn1_per_tkn0(self):
        """Pa and Pb values in units of token 1 per token 0"""
        par , pbr = self.papb_raw
        return (par * self.dec_factor_wei0_per_wei1, pbr * self.dec_factor_wei0_per_wei1)

    @property
    def dec_factor_wei0_per_wei1(self):
        """token wei of token 0 per token wei of token 1 at price=1"""
        return 10 ** (self.tkn0.decimals - self.tkn1.decimals)

    @classmethod
    def _price_f(cls, sp96):
        """price tkn1 per tkn0 in wei units"""
        return sp96 ** 2 / cls.Q192
    
    @property
    def price_tkn1_per_tkn0(self):
        """price of token 1 per token 0 in token units"""
        return self._price_f(self.sp96) * self.dec_factor_wei0_per_wei1
    
    @property
    def L(self):
        """the Uniswap L value, in token units; L**2=k, and k=xy where x,y are virtual token amounts"""
        return self.liquidity / 10 ** (0.5 * (self.tkn0.decimals + self.tkn1.decimals)) if self.liquidity != 0 else 0
    
    def cpc_params(self, **kwargs):
        """
        returns a kwarg dict suitable for CPC.from_univ3
        
        :kwargs:        additional kwargs to return
        """
        pa,pb = self.papb_tkn1_per_tkn0
        pm = self.price_tkn1_per_tkn0
        pmar = pm / pa - 1
        pmbr = pm / pb - 1
        #print("[cpc_params]", pa, pm, pb, pmar, pmbr)
        if pmar < 0:
            #print("[cpc_params] pmar<0; asserting just rounding", pa, pm, pmar)
            assert pmar > -1e-10, f"pm below pa beyond rounding error [{pm}, {pa}, {pmar}]"
        if abs(pmar) < 1e-10:
            #print("[cpc_params] setting pm to pa", pa, pm, pmar)
            pm = pa
        
        if pmbr < 0:
            #print("[cpc_params] pmbr>0; asserting just rounding", pm, pb, pmbr)
            assert pmbr < 1e-10, f"pm abve pb beyond rounding error [{pm}, {pb}, {pmbr}]"
        if abs(pmbr) < 1e-10:
            #print("[cpc_params] setting pm to pb", pm, pb, pmbr)
            pm = pb
            
        result = dict(
            Pmarg = pm,
            uniL = self.L,
            uniPa = pa,
            uniPb = pb,
            pair = self.pair,
            fee = self.fee,
            **kwargs,
        )
        return result
