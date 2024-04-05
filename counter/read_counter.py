import boto3
import os

tableName = os.environ['table_name']

def lambda_handler(event, context):
    visits = get_visits()
    print("1.0 visits from db: ", visits)
    
    visits += 1
    
    print("2.0 update visits to: ", visits)
    update_counter(visits)
    
    visits = get_visits()
    print("3.0 new read of visits from db: ", visits)
    return {
        "isBase64Encoded": false,
        "statusCode": 200,
        "headers": null,
        "body": {"visits": visits}
    }

def get_visits():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)    
    visits = 0
    
    response = table.get_item(Key={'id': 0})
    if "Item" in response:
        if "visits" in response["Item"]:
            visits = response["Item"]["visits"]
    else:
        initialise_visits()
        
    return visits
 
 
def initialise_visits():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)    
    table.put_item(
        Item={
            'id': 0,
            'visits': 0
        }
    )
    
def update_counter(visits):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)    

    print("2.1 visit incremented to: ", visits)
    table.update_item(
        Key={'id': 0},
        UpdateExpression='SET visits = :newcounter',
        ExpressionAttributeValues={
            ':newcounter': visits
        }
    )
    print("2.2 new visit count: ", visits)
