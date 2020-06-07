"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.guestentries = []

        

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guest entries contains: name, streetaddress, city, state, zipcode, storehours, phonenumber, rating, review, price, favorite 
        :return: List of lists
        """
        return self.guestentries

    def insert(self, Name, StreetAddress, City, State, ZipCode, StoreHours, PhoneNumber, Rating, Review, Price, Favorite):
        """
        Appends a new list of values representing new message into guest entries
        :param Name: String
        :param StreetAddress: String
        :param City: String
        :param State: String
        :param Zipcode: String
        :param StoreHours: String
        :param PhoneNumber: String
        :param Rating: String
        :param Review: String
        :param Price: String
        :param Favorite: String
        :return: True
        """
        params = [Name, StreetAddress, City, State, ZipCode, StoreHours, PhoneNumber, Rating, Review, Price, Favorite]
        self.guestentries.append(params)
        return True
