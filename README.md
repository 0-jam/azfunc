# Tutorial of Azure Functions

[Official instructions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python)

---

1. [Environment](#environment)
1. [Installation](#installation)
1. [Configuration](#configuration)
   1. [Create application](#create-application)
   1. [Setting environment variables for your application](#setting-environment-variables-for-your-application)
   1. [Setting environment variables locally](#setting-environment-variables-locally)
      1. [(Optional) Setting environment variables for Python interactive shell](#optional-setting-environment-variables-for-python-interactive-shell)
1. [Usage](#usage)
   1. [azmonkeygen](#azmonkeygen)
   1. [sqltest](#sqltest)

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
1. Install packages by running `$ pipenv install`
1. Enter your new environment by running `$ pipenv shell`
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

### Setting environment variables locally

1. Open SQL Database settings in Azure Portal and allow your client PC's IP address
    - See also: [Azure SQL Database and Azure SQL Data Warehouse IP firewall rules#Create and manage IP firewall rules](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-firewall-configure#create-and-manage-ip-firewall-rules)
1. Open `local.settings.json` and add following lines in the `"Values"` section to run Azure Functions locally:

```json
  "Values": {
    // Another settings above
    "SQL_DB_ENDPOINT": "<Your database endpoint URL>",
    "SQL_DB_NAME": "<The name of your database>",
    "SQL_DB_USERNAME": "<Login name for your database>",
    "SQL_DB_PASSWORD": "<Login password for your database>"
  }
```

#### (Optional) Setting environment variables for Python interactive shell

Create `.env` and add following lines:

```bash
SQL_DB_ENDPOINT='<Your database endpoint URL>'
SQL_DB_NAME='<The name of your database>'
SQL_DB_USERNAME='<Login name for your database>'
SQL_DB_PASSWORD='<Login password for your database>'
```

... and here is how to use:

```
$ python
Python 3.7.6 (default, Feb 13 2020, 16:42:15)
[GCC 9.2.1 20200130] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import settings
>>> import os
>>> os.environ.get('SQL_DB_USERNAME')
'jam'
>>> from sqltest.sql_controller import show_sql
>>> show_sql()
['Road Frames HL Road Frame - Black, 58', 'Road Frames HL Road Frame - Red, 58', ...]
>>>
```

## Usage

The root URL is `https://<your_application>.azurewebsites.net/api` or `http://localhost:7071/api/`

After functions has been deployed, it can be accessed with the following requests:

### azmonkeygen

Based on: [0-jam/sort_algorythms](https://github.com/0-jam/sort_algorythms)/monkey_generator.py

`GET` `/azmonkeygen?gen_size=200`

It returns random strings such as:

```
9A'g0%G)?[\oPAzeqyEnty%tr0}d~iNYa`JtlZb::pQ.ZI1~Uh/r"\xlmp<p\&]~:o>3Ft:1m

1dB	.P^Rh7(w.7R/Wn)jN|0H~szgi)r |d7p
BFAr#- lqkh?G9\S:{`OUg[P_E_[lML.:	$MxEEJcD6AHXk1StI76 Ox)?C@-qDAWY"hW'Tet:u\4 k8k>)7^qk
```

### sqltest

`POST` a JSON to `/sqltest`

```json
{
    "query": "SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid"
}
```
