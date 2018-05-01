import time
import boto3


time_stamp = time.ctime()

client = boto3.resource('dynamodb')

table = client.Table('EdisonSendorDB')

table.put_into(Item={'time':time_stamp,'motion':'True','device':'Jbox001','action':'toggle'})