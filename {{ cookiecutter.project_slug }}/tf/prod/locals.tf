locals {
  env_name = "{{ cookiecutter.environment_prod }}"
  profile  = "{{ cookiecutter.aws_profile_prod }}"
  project  = "{{ cookiecutter.project_slug }}"
  region   = "{{ cookiecutter.aws_region_prod }}"
  repo     = "{{ cookiecutter.project_slug }}"
}
