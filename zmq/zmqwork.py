import zmq

context = zmq.Context()

recver = context.socket(zmq.PULL)
recver.connect('tcp://127.0.0.1:5557')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5558')

while True:
    data = recver.recv()
    sender.send(data)
