<h1 style="text-align: center;">Kamas Dashboard</h1>

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)
![example workflow](https://github.com/clementraoulastek/kamas_dashboard/actions/workflows/dev-continuous-integration.yml/badge.svg)
![example workflow](https://github.com/clementraoulastek/kamas_dashboard/actions/workflows/publish-ghcr.yaml/badge.svg)


This repository aim to display average kamas price from several servers.

## Conda env

A virtual environment is used to run the project. It is managed by conda.

### Create the environment

```bash
conda env create -f environment.yml
```

### Activate the environment

```bash
conda activate kamas-dashboard
```

## Run the app 

### In dev mode
```bash
make run
```

### In prod mode

```bash
make run-prod
```

## Run the tests

```bash
make tests
```

## Deploy the app

### Build the docker image

```bash
make docker-build
```

### Push the docker image

```bash
make docker-push
```

## Create the documentation

```bash
make docs
```




