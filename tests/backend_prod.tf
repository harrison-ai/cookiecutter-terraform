terraform {
  backend "s3" {
    bucket  = "bucket-prod"
    key     = "terraform-cookiecutter"
    region  = "ap-southeast-2"
    profile = "profile-prod"
  }
}
