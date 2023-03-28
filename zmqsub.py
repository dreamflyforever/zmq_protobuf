import zmq
import sys
import google.protobuf

from test_protobuf_pb2 import *

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:8003")

socket.setsockopt_string(zmq.SUBSCRIBE, "")

c = test_data()

print(type(c))

while True:
    msg = socket.recv()
    print(msg)
    c.ParseFromString(msg)
    print(str(c))
    print('success')
    print(type(c))
