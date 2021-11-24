locals {
  env_name = "{{ cookiecutter.environment_dev }}"
  profile  = "{{ cookiecutter.aws_profile_dev }}"
  project  = "{{ cookiecutter.project_slug }}"
  region   = "{{ cookiecutter.aws_region_dev }}"
  repo     = "{{ cookiecutter.project_slug }}"
}
