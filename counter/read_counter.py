import boto3
import os

global table

dynamodb = boto3.resource('dynamodb')
tableName = os.environ['table_name']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    visits = get_visits(table)
    print("1.0 visits from db: ", visits)
    
    visits += 1
    
    print("2.0 update visits to: ", visits)
    update_counter(table, visits)
    
    visits = get_visits(table)
    print("3.0 new read of visits from db: ", visits)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": None,
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
    
def update_counter(table, visits):

    print("2.1 visit incremented to: ", visits)
    table.update_item( 
        Key={'id': 0},
        UpdateExpression='SET visits = :newcounter',
        ExpressionAttributeValues={
            ':newcounter': visits
        }
    )
    print("2.2 new visit count: ", visits)
