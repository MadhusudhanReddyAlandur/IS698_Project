
# AWS PROJECT

# Project Overview

This project automates the deployment and management of a web application infrastructure on AWS using:
-Terraform for creating networking components (VPC, subnets, security groups)
-CloudFormation for deploying EC2, RDS, and Lambda functions
-Python scripts for interacting with EC2, S3, and Lambda services
-Application Load Balancer & Auto Scaling for handling web traffic
-CloudWatch Logs to capture Lambda activity
-DynamoDB for storing application-level data
-S3 and Lambda trigger integration** for upload event logging

## Repository Structure

aws-infra-deployment-project/
    terraform/
        main.tf
        output.tf
    cloudformation/
        infra.yaml
    python-scripts/
        s3.py
        RetrieveEC2.py
        RunningEC2.py
        InvokeLambda.py
    architecture/
        Architecture.png
    README.md

## Setup Instructions

### 1. Clone the Repository
```Terminal
git clone https://github.com/MadhusudhanReddyAlandur/IS698_Project.git
cd AWS_Project
```
### 2. Terraform Networking Setup
```Terminal
cd terraform/
terraform init
terraform apply
```
Creates:
- VPC
- Public & private subnets
- Internet & NAT gateways
- Security groups

### 3. CloudFormation Stack Deployment

```Terminal
cd ../cloudformation/
aws cloudformation deploy --template-file infrastructure.yaml --stack-name WebAppStack
```
Deploys:
- EC2 instance (with Apache & app.py)
- RDS or DynamoDB (depending on use case)
- Lambda function (triggered by S3 upload)

### 4. Flask Web App on EC2

- The EC2 instance hosts a Flask app that inserts entries into DynamoDB.
- The app is accessible via the Application Load Balancer DNS.

### 5. AWS Lambda + S3 Trigger

- When a file is uploaded to the S3 bucket, a Lambda function logs the filename to CloudWatch Logs.
- Python function used:

```python
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    logger.info(f"New file uploaded: {key} in bucket: {bucket}")
```
### 6. Python Scripts via Boto3

Navigate to `python-scripts/` and run:

```bash
python s3.py            # Uploads a test file to S3
python RetrieveEC2.py   # Lists metadata of running EC2
python RunningEC2.py    # Lists all running EC2 instances
python InovkeLambda.py  # Manually invokes Lambda function
```

## Architecture Diagram

![Architecture Diagram](architecture/AWS Archi.png)

## Contributors

- Madhusudhan Reddy Alandur  
- Project guided by: Dr.Samson Oni