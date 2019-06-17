import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5000')
data = 1
while True:
    msg = str(data)
    socket.send(msg)
    data += 5
    time.sleep(1)
    
