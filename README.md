[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)
![example workflow](https://github.com/clementraoulastek/kamas_dashboard/actions/workflows/dev-continuous-integration.yml/badge.svg)
![example workflow](https://github.com/clementraoulastek/kamas_dashboard/actions/workflows/publish-ghcr.yaml/badge.svg)

# Kamas Dashboard

This repository aim to display average kamas price from several servers.

![Screenshot 2024-01-07 at 10-06-30 Kamas Dashboard](https://github.com/clementraoulastek/kamas_dashboard/assets/107399025/af6d9e54-b885-49dc-92c5-9922754ee1eb)

# Conda env

A virtual environment is used to run the project. It is managed by conda.

## Create the environment

```bash
conda env create -f environment.yml
```

## Activate the environment

```bash
conda activate kamas-dashboard
```

# Run the app 

## In dev mode
```bash
make run
```

## In prod mode

```bash
make run-prod
```

# Run the tests

```bash
make tests
```

# Deploy the app

## Build the docker image

```bash
make docker-build
```

## Push the docker image

```bash
make docker-push
```




