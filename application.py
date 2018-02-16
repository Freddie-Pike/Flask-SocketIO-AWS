from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecret'
socket_io = SocketIO(application)


"""
	Socket Routes.
"""

@socket_io.on('grab-field-data')
def grab_field_data(msg):
	emit('append-to-div', msg, broadcast=True)

"""
	Routes
"""
@application.route("/", methods=["POST", "GET"])
def index():
	return render_template("test.html")

@application.route("/socket_page", methods=["POST", "GET"])
def socket_page():
	return render_template("index.html")

if __name__ == '__main__':
	application.debug = True
	socket_io.run(application)

