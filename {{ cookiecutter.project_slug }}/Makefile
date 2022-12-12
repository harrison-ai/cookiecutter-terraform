$(shell if [ -z "${ENV}" ]; then ENV = "dev"; fi)

init:
	terraform -chdir=tf init -backend-config=$(ENV).tfbackend -reconfigure

plan:
	terraform -chdir=tf plan -var-file="$(ENV).tfvars" -no-color -input=false 
