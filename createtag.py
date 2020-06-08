from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Todo(MethodView):
    def get(self):
        return render_template('createtag.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['username'], request.form['bagcolor'], request.form['cellphone'], request.form['description'], request.form['status'])
        return redirect(url_for('index'))
