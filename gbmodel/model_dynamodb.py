from .Model import Model
from datetime import datetime
import boto3
import uuid

tagid = str(uuid.uuid1())

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table('bagtags')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="bagtags",
                KeySchema=[
                    {
                        "AttributeName": "username",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "tagid",
                        "KeyType": "RANGE"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "username",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "tagid",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    def select(self):
        try:
            tagentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.']])

        return([ [f['username'], f['bagcolor'], f['cellphone'], f['description'], f['tagid'], f['status']] for f in tagentries['Items']])

    def insert(self, username, bagcolor, cellphone, description, tagid, status):
        tagitem = {
            'username' : username,
            'bagcolor' : bagcolor,
            'cellphone' : cellphone,
            'description' : description,
            'tagid' : tagid,
            'status' : status
            }

        try:
            self.table.put_item(Item=tagitem)
        except:
            return False

        return True
