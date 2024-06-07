# arb-analyzer

## Clone the repository
git clone --recurse-submodules <url>

## Pull latest changes
make pull

## Install
This repository is using poetry as a package manager, so make sure it is preinstalled on your system.
To install the package and its dependencies run:
```
poetry install
```

## Run
poetry run python -m arb_analyzer.main <input json filename> <output json filename> --dump-curves-path <optional path>

## Run on sample.json
make run

## Run tests
make test

## Run end to end tests
make e2e

## Generate openapi specs
make openapi
