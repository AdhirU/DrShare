import json
import uuid
import time
import boto3


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("DrMentTable")


def lambda_handler(event, context):
    body = json.loads(event['body'])
    res_body = {"code": 1, "output": "Commented Successfully"}
    # Generate UUID for document
    comment_id = str(uuid.uuid4())
    # Put Comment
    table.put_item(
        Item={
            'id': comment_id,
            'comment' : body['comment'],
            'parent_id': body['doc_id'],
            'user_id': body['user_id'],
            'timestamp': int(time.time())
        })
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET",
        },
        "body": json.dumps(res_body),
    }
