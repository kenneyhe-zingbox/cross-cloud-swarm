##General vars
variable "ssh_user" {
  default = "ubuntu"
}

variable "public_key_path" {
  default = "~/.ssh/id_rsa.pub"
}

variable "private_key_path" {
  default = "~/.ssh/id_rsa"
}

##AWS Specific Vars
variable "aws_worker_count" {
  default = 1
}

variable "aws_key_name" {
  default = "YYYY"
}

variable "aws_instance_size" {
  default = "t2.micro"
}

variable "aws_region" {
  default = "us-west-2"
}

variable "access_key" {}

variable "secret_key" {}

