import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print('Connected to server')
    sio.send("connect")

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def message(data):
    print('Message from server: ', data)

# Connect to the server
sio.connect('http://localhost:6000')

# Allow for multiple chat messages
try:
    while True:
        # the client need can input mutil chat message in terminal
        # q: Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v.
        message = input("Enter a message: ")
        if message:
            sio.send(message)
        else:
            sio.send("not-empty")
except KeyboardInterrupt:
    print("Exiting...")

# Wait for responses
sio.wait()

# ---- log --- 一次正常的log -----

# (dlcss) 坚持去λ化(中-易) jim-emacs-fun-py  master @ prun python shell_app/llama_index_shell_client.py
# websocket-client package not installed, only polling transport is available
# Connected to server
# Enter a message: Message from server:  Welcome to the chat!
#
# Enter a message:
# Enter a message: Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v.
# Enter a message: Message from server:  {"message": "The following packages are looking for funding:\n- @material-ui/core\n- @material-ui/styles\n- @material-ui/system\n- webpack\n- schema-utils\n- terser-webpack-plugin\n- webpack-cli\n- browserslist\n- caniuse-lite\n- update-browserslist-db\n- glob\n- base64-js\n- ieee754\n- safe-buffer"}
#
# Enter a message:
#
