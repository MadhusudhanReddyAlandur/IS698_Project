import boto3

s3 = boto3.client('s3')
bucket_name = 'my-boto3-bucket-test-123456'

# Create bucket
s3.create_bucket(Bucket=bucket_name)

# Upload file
s3.upload_file('test.txt', bucket_name, 'test.txt')
print(f"Uploaded test.txt to bucket: {bucket_name}")
