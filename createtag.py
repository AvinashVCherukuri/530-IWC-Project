from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import os
import uuid
from PIL import Image


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
        model.insert(request.form['username'], request.form['bagcolor'], request.form['cellphone'], request.form['description'], tagid, request.form['status'])


        payload = "bg-color=%23ffffff&width=128&fg-color=%23000000&height=128&content=http%3A%2F%2F" + "www.google.com"
        headers = {
                    'x-rapidapi-host': "neutrinoapi-qr-code.p.rapidapi.com",
                    'x-rapidapi-key': QRToken,
                    'content-type': "application/x-www-form-urlencoded"
                    }

        response = requests.request("POST", url, data=payload, headers=headers)
        png = response.text

        imgSize = (703,1248)# the image size
        img = Image.frombytes('L', imgSize, png)
        img.save("foo.jpg")# can give any format you like .png
        
        image = img + ".png"
        return render_template('qr.html',embed_url=image)