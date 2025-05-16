import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

for res in response['Reservations']:
    for inst in res['Instances']:
        print(f"Instance ID: {inst['InstanceId']} - Public IP: {inst.get('PublicIpAddress')}")
