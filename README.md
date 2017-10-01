# cross-cloud-swarm using docker terraform:full
An example of a multi-cloud Docker Swarm on AWS/Google Cloud. Uses Terraform, docker secrets and Ansible to bootstrap.

#### Rough Instructions

*note: This set of scripts assumes that it's running in the default VPC for AWS, as well as using the default network in GCE. These things can be made configurable at some point. PRs welcome.*

##### Bootstrapping with one of the below options
- Source AWS API keys with `source /path/to/awscreds.sh` or `export`
- Configure defaults in `variables.tf` or override them with flags during `terraform apply` or using terraform.tfvars

##### modify main.spy
- Fill and replace terraform.tfvars.template as terraform.tfvars
- Plan the build with `terraform plan` and ensure it looks as expected
- Build the infrastructure with `terraform apply`
- Once built, issue `cat swarm-inventory` to ensure master and workers are populated
- Bootstrap the Swarm cluster with `ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -b -i swarm-inventory swarm.yml`

##### Teardown
- You can tear down the swarm cluster and leave the nodes for rebootstrapping with `ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -b -i swarm-inventory swarm-destroy.yml`
- Destroy all infrastructure with `terraform destroy`


#### best practices with test/build/production
- Testing with "decrypted data with local certificate", vagrant setup and standalone unittest
- Configurable "debugging and vagrant standalone" in github but all daily builds are encrypted and official
- Fully encrypted and official binary
