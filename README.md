# Tutorial of Azure Functions

[Official instructions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python)

---

1. [Environment](#environment)
1. [Installation](#installation)

---

## Environment

- Python 3.7.6 via pyenv
- Initialized environment using pipenv
- Arch Linux x86_64

## Installation

1. Install pyenv and run `$ pyenv install 3.7.6`
    - More information at [pypa/pyenv](https://github.com/pypa/pipenv)
1. Set local Python version by running `$ pyenv local 3.7.6`
1. Initialize pipenv with `$ pipenv --python $(which python)`
1. Enter your new environment by running `$ pipenv shell`
1. Install packages by running `$ pipenv install`
1. Install Azure Functions Core Tools
    - [Azure/azure-functions-core-tools#installing](https://github.com/Azure/azure-functions-core-tools#installing)
    - In Arch Linux, install `azure-functions-core-tools-bin` via AUR
