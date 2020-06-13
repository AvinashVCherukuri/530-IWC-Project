import flask
from index import Index
from createtag import createtag
from viewtag import View
from sendtext import sendtext
from about import About
from qr import Qr


print("Lost My Bag Website @ilostmybags.com Started")

# our Flask app
application = flask.Flask(__name__)

# landing page for the website
application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

# code to see the about page
application.add_url_rule('/about/',
                 view_func=About.as_view('about'),
                 methods=["GET"])

# code when someone submits the form
application.add_url_rule('/submit/',
                 view_func=createtag.as_view('createtag'),
                 methods=['GET', 'POST'])

# code when the qr code is generated
application.add_url_rule('/qr/',
                 view_func=Qr.as_view('qr'),
                 methods=["GET"])

# code when some one veiws list of tags
application.add_url_rule('/viewtag/',
                 view_func=View.as_view('viewtag'),
                 methods=['GET', 'POST'])

# Code for redirecting when some one scans the QR code or when tey send text
application.add_url_rule('/sendtext/<string:id>',
                 view_func=sendtext.as_view('sendtext'),
                 methods=['POST'])


application.add_url_rule('/static/<path:filename>', endpoint='static',view_func=application.send_static_file)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
