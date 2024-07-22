import json
import pandas as pd 
import boto3 
from io import StringIO


s3 = boto3.client('s3')
sns = boto3.client('sns')
sns_arn = 'arn:aws:sns:us-east-1:025066280149:speed-dash-sns:ccf97a4c-a0a6-4013-9c4b-4606ed5544db'

s3_target_bucket = 'speed-dash-target-zone'


def lambda_handler(event, context):
    
    landing_bucket= event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket = landing_bucket,Key =object_key)

    json_data = response['Body'].read().decode('utf-8')
    
    df = pd.read_json(StringIO(json_data))

    df = df[df["status"]== "delivered"]

    s3.put_object(Bucket = s3_target_bucket, Key=f'{object_key[:10]}_delivered.json',Body =df.to_json(orient='records'))

    message = f"Input S3 File {'s3://' + landing_bucket + '/' + object_key} has been processed successfully !! and uploaded to the destination bucket {'s3://' + s3_target_bucket + '/' +f'{object_key[:10]}_delivered.json'}"
    sns.publish(Subject="SUCCESS - Daily Speed Dash Data Processing",TargetArn=sns_arn, Message=message, MessageStructure='text')
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data pipeline Successful!')
    }
