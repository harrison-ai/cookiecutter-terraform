# {{ cookiecutter.project_name}} #

{{ cookiecutter.project_name }} is a terraform module for {{ cookiecutter.project_short_description }}.

## Basic Workflow
This module is structured using [3 musketeers pattern](https://3musketeers.io/) and by default deploys to the development environment, {{ cookiecutter.environment_dev}}; as such in order to deploy the module to the development environment you can run

```bash
make init
make plan
```

After reviewing the output of the plan the module can be deployed to the development environment using

```bash
make apply
```

For deployment into the production environment {{ cookiecutter.environment_prod }} simply comment out the development environment variable in the `.env` file and uncomment out the production environment variable as shown below:

```
# Environment
# ENVIRONMENT={{ cookiecutter.environment_dev }}
ENVIRONMENT={{ cookiecutter.environment_prod }}
```

### AWS credentials
If is expected that your AWS credentials for the environment to be deployed to are available within the `~/.aws/credentials` file under the section {{ cookiecutter.aws_profile_dev}} and/or {{ cookiecutter.aws_profile_prod }} e.g.

```
[{{ cookiecutter.aws_profile_dev }}]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[{{ cookiecutter.aws_profile_prod }}]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

## Build Pipeline

A GitHub Actions job specification is included that will run a Terraform `validate` and Terraform `fmt` command across the entire `./tf` directory.


## What is this repository for?

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## How do I get set up?

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

## Contribution guidelines

* Writing tests
* Code review
* Other guidelines

## Who do I talk to?

* Repo owner or admin {{ cookiecutter.full_name }}({{ cookiecutter.email }})
* Harrison.ai Data Engineering team

## Credits
This repository was created using the [harrison-ai terraform cookiecutter] template (https://github.com/harrison-ai/cookiecutter-terraform)
