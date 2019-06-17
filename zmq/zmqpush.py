import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)

socket.bind('tcp://*:5557')

data = 1
while True:
    msg = str(data)
    socket.send(msg)
    data += 10
    time.sleep(1) 
