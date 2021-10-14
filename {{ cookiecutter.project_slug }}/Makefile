ifneq ($(CI), true)
	include .env
endif

DATESTRING := $(shell date +%FT%H-%M-%S)
.DEFAULT_GOAL := help

TF_DIR = tf/$(ENVIRONMENT)

## init:			terraform init
init: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform init

## init-upgrade:		terraform init -upgrade
init-upgrade: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform init -upgrade

## fmt: 			terraform fmt -recursive
fmt: .env
	docker-compose run --rm --workdir /app terraform fmt -recursive

## ci-fmt:			terraform fmt -recursive -check -diff -write=false
ci-fmt:
	touch .env
	docker-compose run --rm --workdir /app terraform fmt -recursive -check -diff -write=false

## plan:			terraform plan
plan: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform plan

## plan-print:		terraform plan -no-color | tee plan-<date>.out
plan-print: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform plan -no-color | tee plan-${DATESTRING}.out

## apply:			terraform apply
apply: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform apply

## validate: 		terraform validate across all environments
validate:
	./scripts/tf-validate.sh

## destroy:		terraform destroy
destroy: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(TF_DIR) terraform destroy

## tf-shell:		opens a shell inside the terraform container
tf-shell: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --entrypoint='' terraform /bin/ash

## pull:			docker-compose pull
pull:
	docker-compose pull

## .env:			creates .env file with the envvar keys populated
.env:
	touch .env
	docker-compose run --rm envvars envfile --overwrite

## help:			show this help
help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)
