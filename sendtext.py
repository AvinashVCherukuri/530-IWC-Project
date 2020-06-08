from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from twilio.rest import Client
import gbmodel
import os

account_sid = os.environ['twilio_account_sid']
auth_token = os.environ['twilio_auth_token']
Client = Client(account_sid, auth_token)

class sendtext(MethodView):
    def post(self, id):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        text="Hello we found you bag with Tag: %s !" (id)
        model = gbmodel.get_model()
        message = Client.messages.create(
            to="+19716786802",
            from_="+15038511369",
            body=text
        )
        return redirect(url_for('index'))
