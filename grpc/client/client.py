import sys
sys.path.append("../example/gen_py")
import grpc
import data_pb2
import data_pb2_grpc

HOST = '127.0.0.1'
PORT = '19999'


def run():
    with grpc.insecure_channel("{0}:{1}".format(HOST, PORT)) as channel:
        client = data_pb2_grpc.GreeterStub(channel=channel)
        response = client.SayHello(data_pb2.HelloRequest(name='you', message='hey guys'))
    print('received: ' + response.message)

if __name__ == '__main__':
    run()
