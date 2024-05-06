import boto3
import os

global table

dynamodb = boto3.resource('dynamodb')
tableName = os.environ['table_name']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    visits = event.get('visits') 
    update_counter(visits)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": {"visits": visits}
    }    


def update_counter(visits):
    table.update_item(
        Key={'id': 0},
        UpdateExpression='SET visits = :newcounter',
        ExpressionAttributeValues={
            ':newcounter': visits
        }
    )
