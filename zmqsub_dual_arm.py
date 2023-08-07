import zmq
import sys
import google.protobuf

from DualArmCamera_pb2 import *
context = zmq.Context()
socket = context.socket(zmq.SUB)
#socket.connect("tcp://10.1.2.74:8003")
socket.connect("tcp://localhost:8013")

socket.setsockopt_string(zmq.SUBSCRIBE, "")

c = BottlePoses()

print(type(c))

while True:
    msg = socket.recv()
    print(msg)
    c.ParseFromString(msg)
    print(str(c))
    print('success')
    print(type(c))
