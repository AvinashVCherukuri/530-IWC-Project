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
        Each list in guest entries contains: username, bagcolor, cellphone, description, tagid, status 
        :return: List of lists
        """
        return self.guestentries

    def insert(self, username, bagcolor, cellphone, description, tagid, status):
        """
        Appends a new list of values representing new message into guest entries
        :param username, bagcolor, cellphone, description, tagid, status
        :return: True
        """
        params = [username, bagcolor, cellphone, description, tagid, status]
        self.guestentries.append(params)
        return True
