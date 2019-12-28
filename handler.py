import json
import boto3


def connect_handler(event, context):
    return {
        "statusCode": 200
    }


def action_handler(event, context):
    connection_id = event["requestContext"]["connectionId"]

    apigw = get_apigw_management_client(event)

    apigw.post_to_connection(
        ConnectionId=connection_id,
        Data=json.dumps({
            "message": "sample"
        })
    )

    return {
        "statusCode": 200
    }


def disconnect_handler(event, context):
    return {
        "statusCode": 200
    }


def default_handler(event, context):
    return {
        "statusCode": 200
    }


def get_apigw_management_client(context):
    domain = context["requestContext"]["domainName"]
    stage = context["requestContext"]["stage"]

    return boto3.client('apigatewaymanagementapi', endpoint_url=f'https://{domain}/{stage}')
