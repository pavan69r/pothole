import boto3
import datetime

iam_username = 'Pavan'
iam_password = "*ZlH{6f'"
region_name = 'eu-north-1'
def send_to_cloud(curl,region_name='eu-north-1'):
    table_name = 'sessions'
    dynamo_db = boto3.client('dynamodb',region_name=region_name)
    res=None
    for i in curl:
        s, val = i.popitem()
        x = str(datetime.datetime.now())
        item_scarface = {
            'sid': {'N': str(s)},
            'latitude': {'N': str(val[0])},
            'longitude': {'N': str(val[1])},
            'number_of_pothole': {'N': str(val[2])},
            'date&time': {'S': x}
        }
        if __name__ == "__main__":
            res = dynamo_db.put_item(TableName=table_name, Item=item_scarface)
    return res

def get_from_cloud():
    dynamo_db = boto3.resource('dynamodb',region_name=region_name,aws_access_key_id=iam_username,aws_secret_access_key=iam_password)
    table_name = 'sessions'
    table = dynamo_db.Table(table_name)
    response = table.scan()
    item = response['Items']
    if item:
        return item
    else:
        return None
    
res = send_to_cloud([{3: [27.2514, 81.6296, 2]}, {4: [28.38, 65.12, 8]},{5:[25.4358,81.8263,56]},{6:[22.3176,82.9739,45]}])