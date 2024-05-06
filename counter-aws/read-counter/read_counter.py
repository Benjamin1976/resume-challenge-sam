import boto3
import os

global table

dynamodb = boto3.resource('dynamodb')
tableName = os.environ['table_name']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    visits = get_visits(table)
    print("3.0 new read of visits from db: ", visits)
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

def get_visits(table):
    visits = 0
    response = table.get_item(Key={'id': 0})
    if "Item" in response:
        if "visits" in response["Item"]:
            visits = response["Item"]["visits"]
    else:
        initialise_visits(table)
        
    return visits
 
 
def initialise_visits(table):
    table.put_item(Item={
            'id': 0,
            'visits': 0
        })

