from flask import render_template
from flask.views import MethodView
import gbmodel

class View(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(username=row[0], bagcolor=row[1], cellphone=row[2], description=row[3], tagid=row[4], status=row[5]) for row in model.select()]
        return render_template('viewtag.html', entries=entries)
