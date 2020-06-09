from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import os
import uuid


QRToken = os.environ['qrapi']
url = "https://neutrinoapi-qr-code.p.rapidapi.com/qr-code"

tagid = str(uuid.uuid1())

class createtag(MethodView):
    def get(self):
        return render_template('createtag.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['username'], request.form['bagcolor'], request.form['cellphone'], request.form['description'], request.form['status'], request.form['tagid'])


        payload = "bg-color=%23ffffff&width=128&fg-color=%23000000&height=128&content=http%3A%2F%2F" + "here" + tagid
        headers = {
                    'x-rapidapi-host': "neutrinoapi-qr-code.p.rapidapi.com",
                    'x-rapidapi-key': QRToken,
                    'content-type': "application/x-www-form-urlencoded"
                    }

        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        embed_url = response.data[0].embed_url

        return redirect(url_for('index'))
        return render_template('index.html',embed_url=embed_url)