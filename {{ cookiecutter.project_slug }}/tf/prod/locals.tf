locals {
  region   = "{{ cookiecutter.aws_region_prod }}"
  profile  = "{{ cookiecutter.aws_profile_prod }}"
  project  = "{{ cookiecutter.project_slug }}"
  env_name = "{{ cookiecutter.environment_prod }}"
}
