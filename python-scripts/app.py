import boto3
import time

app = Flask(__name__)

@app.route('/')
def home():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('UsersTable')
    response = table.put_item(Item={
        'userId': 'visitor',
        'timestamp': str(time.time())
    })
    return "<h1>Hello from EC2 Web Server!</h1><p>Record written to DynamoDB.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
