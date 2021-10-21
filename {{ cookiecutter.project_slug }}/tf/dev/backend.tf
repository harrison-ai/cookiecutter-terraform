terraform {
  backend "s3" {
    bucket  = "{{ cookiecutter.backend_bucket_dev }}"
    key     = "{{ cookiecutter.project_slug }}-{% now 'utc', '%Y-%m-%d' %}/{{ cookiecutter.environment_dev }}/tfstate"
    region  = "{{ cookiecutter.aws_region_dev }}"
    profile = "{{ cookiecutter.aws_profile_dev }}"
  }
}
