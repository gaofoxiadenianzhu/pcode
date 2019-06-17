import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

data = 1
while True:
    socket.send(str(data))
    response = socket.recv()
    print(response)
    data += 10
    time.sleep(1)
    
