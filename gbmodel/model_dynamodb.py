from .Model import Model
from datetime import datetime
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table('FoodCart')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="FoodCart",
                KeySchema=[
                    {
                        "AttributeName": "StoreHours",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "Name",
                        "KeyType": "RANGE"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "StoreHours",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "Name",
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
            gbentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.']])

        return([[f['Name'], f['StreetAddress'], f['City'], f['State'], f['Zipcode'], f['StoreHours'], f['PhoneNumber'], f['Rating'], f['Review'], f['Price'], f['Favorite']] for f in gbentries['Items']])

    def insert(self,Name, StreetAddress, City, State, Zipcode, StoreHours, PhoneNumber, Rating, Review, Price, Favorite):
        gbitem = {
            'Name' : Name,
            'StreetAddress' : StreetAddress,
            'City' : City,
            'State' : State,
            'Zipcode' : Zipcode,
            'StoreHours' : StoreHours,
            'PhoneNumber' : PhoneNumber,
            'Rating' : Rating,
            'Review' : Review,
            'Price' : Price,
            'Favorite' : Favorite
            }

        try:
            self.table.put_item(Item=gbitem)
        except:
            return False

        return True
