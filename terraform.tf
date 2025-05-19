# vulnerable-resources.tf
provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "vulnerable_bucket" {
  bucket = "vulnerable-bucket-example"
  acl    = "public-read"  # Security issue: Public access
  
  # Security issue: No encryption
  # Missing server_side_encryption_configuration
  
  # Security issue: No versioning
  # Missing versioning block
  
  # Security issue: No logging
  # Missing logging block
}

resource "aws_security_group" "vulnerable_sg" {
  name        = "vulnerable-sg"
  description = "Allow all inbound traffic"
  
  # Security issue: Open to the world
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Security issue: Open egress
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
