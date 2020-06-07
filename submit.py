from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Submit(MethodView):
    def get(self):
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['Name'], request.form['StreetAddress'], request.form['City'], request.form['State'], request.form['Zipcode'], request.form['StoreHours'], request.form['PhoneNumber'], request.form['Rating'], request.form['Review'], request.form['Price'], request.form['Favorite'])
        return redirect(url_for('index'))
