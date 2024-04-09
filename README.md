# ci-cd-example

Running CI/CD with pipeline-ai.

## Setup

This repo demonstrates a production and staging oriented deployment system for using the pipeline-ai SDK. It also includes some git hooks integration for ensuring all code is properly formatted and linted before being pushed to the repository.

To being you need to install poetry and the dependencies for this project:

```bash
pip install -U poetry
poetry install
```

You then need to install the pre-commit hooks for this project:

```bash
./setup.sh
```

## Github actions secrets

- `PIPELINE_API_TOKEN` - This is the token used to authenticate with Mystic.ai
