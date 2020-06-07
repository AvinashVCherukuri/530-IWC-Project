"""
A simple guestbook flask application.
"""
import flask
from flask.views import MethodView
from index import Index
from submit import Submit
from view import View

application = flask.Flask(__name__)       # our Flask app

application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

application.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

application.add_url_rule('/view',
                 view_func=View.as_view('view'),
                 methods=["GET"])

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
