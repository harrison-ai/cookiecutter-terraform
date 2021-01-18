locals {
  region   = "{{ cookiecutter.aws_region_dev }}"
  profile  = "{{ cookiecutter.aws_profile_dev }}"
  project  = "{{ cookiecutter.project_slug }}"
  env_name = "{{ cookiecutter.environment_dev }}"
}
