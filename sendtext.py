from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from twilio.rest import Client
import gbmodel
import os
from ipdata import ipdata
from flask import request
import json

account_sid = os.environ['twilio_account_sid']
auth_token = os.environ['twilio_auth_token']
ipdata_key = os.environ['ipdata_api_key']
Client = Client(account_sid, auth_token)
ipdata = ipdata.IPData(ipdata_key)

class sendtext(MethodView):
    def post(self, id):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        # Create an instance of an ipdata object.
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            ip = request.remote_addr
        response = ipdata.lookup(ip)
        city = response['city']
        country_name = response['country_name']

        text="Hello we found you bag with Tag: %s at City: %s, country: %s use by IP:!" % (str(id),city,country_name,ip)
        model = gbmodel.get_model()
        message = Client.messages.create(
            to="+19716786802",
            from_="+12679152751",
            body=text
        )
        return redirect(url_for('index'))
