# Backend API

The backend of the application consists of an API written in [FastAPI](https://fastapi.tiangolo.com/).

## Running locally

1. Inside the `ROOT` directory, create a new virtual Python environment: `python{{cookiecutter.runtime}} -m venv venv` (only do this once - you can reuse the same virtual environment each time you run the server). If your system doesn't have python {{cookiecutter.runtime}}, install it from [Python.org](https://www.python.org/downloads/).
1. Activate the virtual environment: python`. venv/bin/activate`
1. Update pip: `pip install -U pip`
1. Install the server dependencies: `pip install -r requirements.txt`
1. Run the server: `uvicorn app.api.main:app` or use `python main.py`
 

> [!IMPORTANT]  
> For the API to function, you must have an `.env` file in this directory which holds API keys and application secrets. Please contact {{cookiecutter.contact_name}} ({{cookiecutter.contact_email}}) for the contents of this file.


## API documentation

The API is documented using [Swagger](https://swagger.io/). To view the documentation, run the server and navigate to `/docs` or `/redoc`.


## API Testing from CLI

Using a Curl statement, pass in the api token key with the added `authorizationToken` header.
```python

# Replace [#AWS API Service ID#] with corresponding Id and included AWS Region and deploy stage(development, production, etc.)
curl --location 'https://[#AWS API Service ID#].execute-api.{{cookiecutter.aws_region_name}}.amazonaws.com/{{cookiecutter.aws_deploy_stage}}/' \
--header 'authorizationToken: {{cookiecutter.api_token_key}}'

# Example usage
curl --location 'https://onwt6hv9kk.execute-api.{{cookiecutter.aws_region_name}}.amazonaws.com/{{cookiecutter.aws_deploy_stage}}/' \
--header 'authorizationToken: {{cookiecutter.api_token_key}}'

```

## Code formatting

Before committing changes to Github, perform code formatting/linting using [Black](https://black.readthedocs.io/en/stable/) with `black .`.


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
