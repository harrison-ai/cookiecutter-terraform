ENVIRONMENT := $(shell grep ENVIRONMENT .env | awk -F '=' '{print $$2}')
DATESTRING := $(shell date +%FT%H-%M-%S)
.DEFAULT_GOAL := help

ifeq ($(ENVIRONMENT), dev)
	DIR := tf/dev
else ifeq ($(ENVIRONMENT), prod)
	DIR := tf/prod
endif

## init:			terraform init
init: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform init

## init-upgrade:		terraform init -upgrade
init-upgrade: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform init -upgrade

## fmt: 			terraform fmt -recursive
fmt:
	docker-compose run --rm terraform fmt -recursive tf

## plan:			terraform plan
plan: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform plan

## plan-print:		terraform plan -no-color | tee plan-<date>.out
plan-print: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform plan -no-color | tee plan-${DATESTRING}.out

## apply:			terraform apply
apply: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform apply

## destroy:		terraform destroy
destroy: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform destroy

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
