from flask import redirect, request, url_for, render_template
from flask.views import MethodView

class About(MethodView):
    def get(self):
        return render_template('about.html')