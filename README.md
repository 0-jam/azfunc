# Tutorial of Azure Functions

[Official instructions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python)

---

1. [Environment](#environment)
1. [Installation](#installation)
1. [Configuration](#configuration)
   1. [Create application](#create-application)
   1. [Setting environment variables for your application](#setting-environment-variables-for-your-application)

---

## Environment

- Python 3.7.6 via pyenv
- Initialized local environment using pipenv
- Arch Linux x86_64
- Visual Studio Code 1.42.1

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
1. Install 'Azure Account', and 'Azure Functions' extensions in your VSCode

## Configuration

### Create application

1. [Create an Azure Functions app](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python)
    - It also shows how to deploy your application
1. [Create a SQL Database](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-single-database-get-started?tabs=azure-portal) **with a public endpoint**

### Setting environment variables for your application

1. Enter Azure Portal
1. 'Function App' -> your application
1. 'Platform features' tab -> 'Configuration'
1. 'Application Settings' -> 'New application setting' and add followings:
    - SQL_DB_ENDPOINT
        - Your database endpoint URL
    - SQL_DB_NAME
        - The name of your database
        - You can see URL and the name of your database in the Azure Portal
    - SQL_DB_USERNAME
        - User's login name for your database
    - SQL_DB_PASSWORD
        - User's login password for your database
    - See also: [Quickstart: Use Python to query an Azure SQL database](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python?tabs=ubuntu)
