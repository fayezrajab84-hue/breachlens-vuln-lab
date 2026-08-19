# DELIBERATELY VULNERABLE — BreachLens IaC (Checkov) test target. Do NOT apply.

provider "aws" {
  region = "us-east-1"
}

# IaC: public-read bucket, no encryption, no logging, no versioning.
resource "aws_s3_bucket" "data" {
  bucket = "breachlens-vuln-lab-data"
  acl    = "public-read"
}

# IaC: security group leaves SSH (22) open to the entire internet.
resource "aws_security_group" "open_ssh" {
  name = "open-ssh"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# IaC: RDS instance unencrypted + publicly accessible + hardcoded password + no backups.
resource "aws_db_instance" "default" {
  allocated_storage   = 10
  engine              = "mysql"
  instance_class      = "db.t3.micro"
  username            = "admin"
  password            = "hardcoded-db-password"
  publicly_accessible = true
  storage_encrypted   = false
  skip_final_snapshot = true
}
