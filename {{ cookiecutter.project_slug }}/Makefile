ENVIRONMENT := $(shell grep ENVIRONMENT .env | awk -F '=' '{print $$2}')
DATESTRING := $(shell date +%FT%H-%M-%S)

ifeq ($(ENVIRONMENT), dev)
	DIR := tf/dev
else ifeq ($(ENVIRONMENT), prod)
	DIR := tf/prod
endif

init: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform terraform init

fmt:
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm terraform terraform fmt -recursive tf

plan: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform terraform plan

plan-print: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform terraform plan -no-color | tee plan-${DATESTRING}.out

apply: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform terraform apply

destroy: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm --workdir /app/$(DIR) terraform terraform destroy

tf-shell: .env
	docker-compose run --rm envvars ensure --tags terraform
	docker-compose run --rm terraform /bin/ash

pull:
	docker-compose pull

package:
	./scripts/package.sh

.env:
	touch .env
	docker-compose run --rm envvars envfile --overwrite
