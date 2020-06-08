from flask import render_template
from flask.views import MethodView
import gbmodel

class View(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(Name=row[0], StreetAddress=row[1], City=row[2], State=row[3], Zipcode=row[4], StoreHours=row[5], PhoneNumber=row[6], Rating=row[7], Review=row[8], Price=row[9], Favorite=row[10] ) for row in model.select()]
        return render_template('viewtag.html', entries=entries)
