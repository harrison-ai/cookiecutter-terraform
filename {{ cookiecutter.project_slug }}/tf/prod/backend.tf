terraform {
  backend "s3" {
    bucket  = "{{ cookiecutter.backend_bucket_prod }}"
    key     = "{{ cookiecutter.project_slug }}-{% now 'utc', '%Y-%m-%d' %}/{{ cookiecutter.environment_prod }}/tfstate"
    region  = "{{ cookiecutter.aws_region_prod }}"
    profile = "{{ cookiecutter.aws_profile_prod }}"
  }
}
