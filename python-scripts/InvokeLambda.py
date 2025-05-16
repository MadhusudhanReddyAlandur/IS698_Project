import boto3
import json

# Initialize AWS clients
s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

# Update these with your details
LAMBDA_FUNCTION_NAME = 'S3UploaderLogger'
BUCKET_NAME = 'webapp-upload-logs-madhu'

# List all objects in the S3 bucket
response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

# Check if bucket has contents
if 'Contents' not in response:
    print(f"No files found in bucket: {BUCKET_NAME}")
    exit()

# Loop through each file and invoke Lambda
for obj in response['Contents']:
    object_key = obj['Key']
    print(f"\nInvoking Lambda for: {object_key}")

    # Simulated S3 event payload
    event_payload = {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "s3": {
                    "bucket": {
                        "name": BUCKET_NAME
                    },
                    "object": {
                        "key": object_key
                    }
                }
            }
        ]
    }

    # Invoke Lambda
    lambda_response = lambda_client.invoke(
        FunctionName=LAMBDA_FUNCTION_NAME,
        InvocationType='RequestResponse',
        Payload=json.dumps(event_payload)
    )

    # Print Lambda's response
    print("Lambda response:")
    print(lambda_response['Payload'].read().decode())


