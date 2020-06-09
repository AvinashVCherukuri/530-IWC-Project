from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from twilio.rest import Client #twilio api for sending text message
import gbmodel
import os
from ipdata import ipdata # Ipdata api to look up IPGeo Data
from flask import request
import json

# get API keys for twilio from enviorment variable
account_sid = os.environ['twilio_account_sid']
auth_token = os.environ['twilio_auth_token']

# get API key for ipdata from environment variable
ipdata_key = os.environ['ipdata_api_key']

# Create an instance of an twilio client object.
Client = Client(account_sid, auth_token)

# Create an instance of an ipdata object.
ipdata = ipdata.IPData(ipdata_key)

class sendtext(MethodView):
    def post(self, id):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        id: Tagid of bag sent from sendText button
        It will lookup Client's IP and tracke GeoIP location, send message to registered user with IP GeoLocationa and TagID.
        """
        # Get Client/visitor's IP.
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            ip = request.remote_addr
        
        # if app is running on localhost, it will get 127.0.0.1 which private ip and cannot find IpGeo data. So taking default PublicIP
        if ip == '172.17.0.1' or ip == '127.0.0.1':
            ip = '76.27.220.107'
        
        #look GeoDat from IP
        response = ipdata.lookup(ip)
        # From response we can get lot more Geo data, for here just taking CIty and Country.
        city = response['city']
        country_name = response['country_name']
        
        # Preparing text for sending message
        text="Hello we found you bag with Tag: %s at City: %s, country: %s use by IP:%s !" % (str(id),str(city),str(country_name),str(ip))
        model = gbmodel.get_model()
        
        # sending text to below number for twilio client
        message = Client.messages.create(
            to="+19716786802",
            from_="+12679152751",
            body=text
        )
        return redirect(url_for('index'))
