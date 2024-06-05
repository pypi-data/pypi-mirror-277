# cicd-greetings
Application to greet and talk
Here's the complete README file that includes instructions for setting up unit testing, GitHub Actions workflow for automation, and deployment to PyPI.

```markdown
# Greetings Package

This project is a simple Python package that provides a CLI for greeting users and multiplying numbers. The package is built with setuptools and includes unit tests, GitHub Actions CI/CD pipeline for automated testing, and deployment to PyPI.

## Directory Structure

```
greetings/
├── .github/
│   └── workflows/
│       └── python-package.yml
├── greetings/
│   ├── __init__.py
│   └── cli.py
├── tests/
│   └── test_hello_world.py
├── setup.py
├── setup.cfg
├── MANIFEST.in
├── README.md
└── LICENSE
```

## Setup

### Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:yourusername/greetings.git
    cd greetings
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -e .
    ```

### Running the CLI

To use the CLI, run the following command:

```sh
greetings-cli --greet
greetings-cli --multi 2,3,4
```

## Unit Testing

To run unit tests:

1. Edit the `tests/test_hello_world.py` file as needed to add or modify tests.

2. Run the tests:
    ```sh
    python -m unittest discover tests
    ```

## GitHub Actions CI/CD

The CI/CD pipeline is configured to automatically run tests and deploy the package to PyPI on push and pull request events.

### YAML File for GitHub Actions

Create a `.github/workflows/python-package.yml` file with the following content:

```yaml
name: Python package

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel
        pip install -e .
    - name: Run tests
      run: |
        python -m unittest discover tests
    - name: Build and deploy to PyPI
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python setup.py sdist bdist_wheel
        python -m pip install twine
        python -m twine upload --skip-existing dist/*
```

### Adding Secrets to GitHub

1. Go to your GitHub repository.
2. Click on `Settings`.
3. In the left sidebar, click on `Secrets`.
4. Click on `New repository secret`.
5. Add the following secrets:

   - `PYPI_USERNAME`: Your PyPI username (e.g., `deshitha`).
   - `PYPI_PASSWORD`: Your PyPI API token.

## Committing and Pushing Changes

1. Add changes:
    ```sh
    git add .
    ```

2. Commit changes:
    ```sh
    git commit -m "message"
    ```

3. Push changes:
    ```sh
    git push
    ```

This will trigger the GitHub Actions workflow to run tests and deploy the package to PyPI if the tests pass.
```

This README file covers the setup, usage, unit testing, and CI/CD pipeline configuration with GitHub Actions, including deployment to PyPI. Adjust the repository URLs, usernames, and other details as needed for your specific setup.