#!/bin/bash

set -eu

CI=${CI:-false}

ENVS=$(find tf -maxdepth 1 -mindepth 1 -type d | egrep -v '(modules|terraform)')

for ENV in ${ENVS[@]}; do
  if [[ ${CI} == 'true' ]]
  then
    echo "validating environment ${ENV} in CI"
    terraform -chdir=${GITHUB_WORKSPACE}/${ENV} init -backend=false
    terraform -chdir=${GITHUB_WORKSPACE}/${ENV} validate -json
  else
    echo "validating environment ${ENV}"
    docker-compose run --rm --workdir /app/${ENV} terraform init -backend=false
    docker-compose run --rm --workdir /app/${ENV} terraform validate -json
  fi
done
