from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Store connected users
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    if 'sid' in users:
        username = users['sid']
        del users['sid']
        emit('user_left', {'username': username}, broadcast=True)
        print(f'{username} disconnected')

@socketio.on('new_user')
def handle_new_user(username):
    users['sid'] = username
    emit('user_joined', {'username': username}, broadcast=True)
    print(f'{username} joined the chat')

@socketio.on('new_message')
def handle_new_message(message):
    username = users.get('sid', 'Anonymous')
    emit('chat_message', {'username': username, 'message': message}, broadcast=True)
    print(f'{username}: {message}')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)