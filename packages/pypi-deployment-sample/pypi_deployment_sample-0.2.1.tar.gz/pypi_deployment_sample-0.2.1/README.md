## pypi-deployment-sample

This repository contains a deployment sample of a Python Pacakge (with poetry) via Github Actions to PYPI

The workflow assumes that you have "POETRY_PYPI_TOKEN_PYPI" secrets configured

Actions Summary:
- Installs Python and Setup poetry
- Bumps up a "patch" version
- Build & Publish to PYPI
- Creates and Pushes a commit and a git tag with new bumped version
