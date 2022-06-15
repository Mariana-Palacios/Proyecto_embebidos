from urllib import response
import boto3

dynamo_client = boto3.resource('dynamodb')
tabla = dynamo_client.Table('datalogs')

payload = {
"id": "1",
"temperatura": "30",
"unidad temperatura": "Centigrados",
"velocidad del viento": "10",
"unidad velocidad": "km/h"
}

response = tabla.put_item(
    Item = payload
)

print(response)
