from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import os
import uuid
import urllib.request
import shutil
from os import listdir
from os.path import isfile, join

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

        url = "http://api.qrserver.com/v1/create-qr-code/?data=" + "http://ilostmybags.ipq.co/sendtext/" + tagid + "&size=100x100"

        """
        This function takes in the url for the api request. 
        It fist removes all the files in the statisc folder with .jpg extension and then download the new jpg qr code and places it in the statis folder.
        """
        def download_image(url):
            location = os.getcwd() + "/static"
            onlyfiles = [f for f in listdir(location) if isfile(join(location, f))]

            for tryfile in onlyfiles:
                if ".jpg" in tryfile:
                    tryfile = location + "/" + tryfile
                    os.remove(tryfile)

            file = tagid + ".jpg"
            urllib.request.urlretrieve(url, file)
            shutil.move(file, location)

            return file

        image = download_image(url)

        return render_template('qr.html',embed_url=image)