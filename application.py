"""
A simple bagtracking flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from createtag import Todo

application = flask.Flask(__name__)       # our Flask app

application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

application.add_url_rule('/static/<path:filename>',endpoint='static',view_func=application.send_static_file) 

application.add_url_rule('/createtag/',
                 view_func=Todo.as_view('createtag'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
    print (request.remote_addr)
