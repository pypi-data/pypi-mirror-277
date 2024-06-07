import logging
import time

import click

from .config import setup
from .runner import Runner
from .interfaces.input import Input


logger = logging.getLogger(__name__)


@click.command()
@click.argument("input_fp", type=click.File("r"))
@click.argument("output_fp", type=click.File("w"))
@click.option("--dump-curves-path", "dump_curves_fp", type=click.File("w"), help="Location to which to dump optimizer ready curves.")
def main(input_fp, output_fp, dump_curves_fp):
    logger.info("Timing - process startup %f", time.process_time())
    ts = time.perf_counter()
    input = Input.model_validate_json(input_fp.read())
    logger.info("Timing - json parsing %f", time.perf_counter() - ts)
    runner = Runner(input, dump_curves_fp)
    output = runner.run()
    output_fp.write(output.model_dump_json(
        indent=2,
        exclude_none=True,
    ))


if __name__ == "__main__":
    setup()
    main()
