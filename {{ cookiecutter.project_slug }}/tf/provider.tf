terraform {
  required_version = ">= 1.0.10"

  backend "s3" {}

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region  =  var.region
  profile = var.CI ? "" : var.profile

  default_tags {
    tags = {
      Repo = var.repo
    }
  }
}
