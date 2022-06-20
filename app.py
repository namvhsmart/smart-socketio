from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('vehicle message')
def broadcast_vehicle(data):
    emit('vehicles', data, broadcast=True)


@socketio.on('event message')
def broadcast_event(data):
    emit('event', data, broadcast=True)


@app.route('/api/vehicles', methods=['POST'])
def vehicle():
    data = request.json
    emit('vehicles', data, broadcast=True, namespace='/')
    return 'OK'


@app.route('/api/event', methods=['POST'])
def event():
    data = request.json
    emit('event', data, broadcast=True, namespace='/')
    return 'OK'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
