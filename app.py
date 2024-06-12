from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('offer')
def handle_offer(offer):
    emit('offer', offer, broadcast=True)

@socketio.on('answer')
def handle_answer(answer):
    emit('answer', answer, broadcast=True)

@socketio.on('candidate')
def handle_candidate(candidate):
    emit('candidate', candidate, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True,host='0.0.0.0')
