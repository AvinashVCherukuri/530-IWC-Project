from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Qr(MethodView):
    def get(self):
        return render_template('qr.html')