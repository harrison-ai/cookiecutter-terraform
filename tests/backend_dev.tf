terraform {
  backend "s3" {
    bucket  = "bucket-dev"
    key     = "terraform-cookiecutter"
    region  = "ap-southeast-2"
    profile = "profile-dev"
  }
}
