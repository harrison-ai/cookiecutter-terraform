# cookiecutter-terraform

<!-- [![image]][1] -->

<!-- [![Documentation Status]][2] -->

-   Free software: BSD 3 Clause License 
<!-- -   Documentation: <https://cookiecutter-terraform.readthedocs.io>. -->

## Features

- Terraform template as per [harrison.ai](https://www.harrison.ai/) style guide
- Automatically populate configuration details for development and production environments
- [3 musketeers](https://3musketeers.io/) pattern usage


## Docker Usage

1. `make docker-build` - Build the Docker image
2. `make cookiecutter` - Launch the cookiecutter wizard

Once the wizard completes, the new cookiecutter'ed repo will exist in the root of this repo.  Move it to your desired location

## Usage

1. First install cookiecutter via `pip install cookiecutter`
2. Call cookiecutter using this template `cookiecutter https://github.com/harrison-ai/cookiecutter-terraform`
3. Answer the questions in the prompt, the values within the square brackets are the provided defaults.  Press the enter key to use the default value.
4. The newly created module will be in the directory with the same name as the entered *project_slug*.

e.g.
```bash
$ pip install cookiecutter
Collecting cookiecutter
  Using cached cookiecutter-1.7.2-py2.py3-none-any.whl (34 kB)
... truncated
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 arrow-0.17.0 binaryornot-0.4.4 certifi-2020.12.5 chardet-4.0.0 click-7.1.2 cookiecutter-1.7.2 idna-2.10 jinja2-time-0.2.0 poyo-0.5.0 python-dateutil-2.8.1 python-slugify-4.0.1 requests-2.25.1 six-1.15.0 text-unidecode-1.3 urllib3-1.26.2

$ cookiecutter https://github.com/harrison-ai/cookiecutter-terraform
full_name [me]: John Citizen
email [me@there.com]: john@citizen.com
project_name [Terraform Cookiecutter]: aws-vpc
project_slug [aws-vpc]:
project_short_description [providing all the boilerplate you need to create a terraform package.]: builds a standard AWS VPC
aws_profile_prod [profile-prod]: datalake-prod
aws_profile_dev [datalake-dev]:
aws_region_prod [ap-southeast-2]:
aws_region_dev [ap-southeast-2]:
environment_prod [env-prod]: company-prod
environment_dev [company-dev]:
backend_bucket_prod [bucket-prod]: terraform-backend-prod
backend_bucket_dev [terraform-backend-dev]:
buildkite_agent [buildkite-agent]:
version [0.1.0]:
create_author_file [y]:
Select open_source_license:
1 - Not open source
2 - MIT license
3 - BSD license
4 - ISC license
5 - Apache Software License 2.0
6 - GNU General Public License v3
Choose from 1, 2, 3, 4, 5, 6 [1]:

$ tree aws-vpc
aws-vpc
├── CHANGELOG.md
├── docker-compose.yml
├── envvars.yml
├── Makefile
├── README.md
└── tf
    ├── data.tf
    ├── dev
    │   ├── backend.tf
    │   ├── data.tf
    │   ├── locals.tf
    │   ├── main.tf
    │   └── provider.tf
    ├── main.tf
    ├── prod
    │   ├── backend.tf
    │   ├── data.tf
    │   ├── locals.tf
    │   ├── main.tf
    │   └── provider.tf
    └── provider.tf

3 directories, 18 files
```

### Alternative Defaults

As described in the [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html) you can also override some of the defaults using additional **default_context** into a yaml file and passing the file either via the cli or an environment variable e.g:

Example config:

```yaml
default_context:
  full_name: John Citizen
  email: john@citizen.com
  aws_profile_prod: datalake-prod
```
then using either

```bash
cookiecutter --config-file /path/to/config.yaml https://github.com/harrison-ai/cookiecutter-terraform
```
or

```bash
export COOKIECUTTER_CONFIG=/path/to/config.yaml
cookiecutter https://github.com/harrison-ai/cookiecutter-terraform
```


## Credits

This package was created with [Cookiecutter] and influenced by the
[audreyr/cookiecutter-pypackage] project template.

  <!-- [image]: https://img.shields.io/pypi/v/cookiecutter_terraform.svg -->
  <!-- [1]: https://pypi.python.org/pypi/cookiecutter_terraform -->
  <!-- [Documentation Status]: https://readthedocs.org/projects/cookiecutter-terraform/badge/?version=latest -->
  <!-- [2]: https://cookiecutter-terraform.readthedocs.io/en/latest/?badge=latest -->
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [audreyr/cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage
