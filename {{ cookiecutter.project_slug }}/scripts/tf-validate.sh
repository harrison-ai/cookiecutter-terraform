#!/bin/bash

set -eu

ENVS=$(find tf -maxdepth 1 -mindepth 1 -type d)

for ENV in ${ENVS[@]}
do
  echo "Validating environment ${ENV}"
  docker-compose run --rm --workdir /app/${ENV} terraform terraform init -backend=false
	docker-compose run --rm --workdir /app/${ENV} terraform terraform validate -json
done
