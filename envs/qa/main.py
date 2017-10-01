#!python

"""
Wrapper to setup infrastructure with docker swarm and node in AWS
"""
import subprocess


def docker_add_secret(secret, filename):
    """
    create secrets for swarm master
    """
    try:
        cmd = "docker secret create {0} {1}".format(secret, filename)
        subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError:
        return 1
    return 0


def docker_cleanup(name):
    """
    cleanup any with name 
    """
    cmd = "docker service rm " + name
    return subprocess.check_output(cmd.split())


def docker_help(name, secret):
    """
    run terraform plan
    """

    cmd = "docker service create  --detach=false -t --mount type=bind,source=${{PWD}},destination=/data -w /data " \
          "--name {0} --secret {1} --restart-condition none hashicorp/terraform:0.10.6 --help".format(name, secret)
    return subprocess.check_output(cmd.split())


def docker_plan(name, secret, filename, plan):
    """
    run terraform plan
    """

    cmd = "docker service create  --detach=false -t --mount type=bind,source=${{PWD}},destination=/data -w /data " \
          "--name {0} --secret {1} --restart-condition none hashicorp/terraform:0.10.6 plan -var-file=/run/secrets/{2}" \
          " -out {3}".format(name, secret, filename, plan)
    return subprocess.check_output(cmd.split())


def terra_plan(filename, plan):
    """
    run terraform plan
    """
    cmd = "terraform init"
    subprocess.check_output(cmd.split())

    cmd = "terraform plan -var-file={0} -out {1}".format(filename, plan)
    return subprocess.check_output(cmd.split())


if __name__ == "__main__":
    # assume local tfstate
    terra_plan("terraform.tfvars", "plan.out")
