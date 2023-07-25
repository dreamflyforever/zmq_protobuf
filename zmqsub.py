import zmq
import sys
import google.protobuf

from rgbd_repeat_pb2 import *
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://0.0.0.0:8003")

socket.setsockopt_string(zmq.SUBSCRIBE, "")

c = pose_array()

print(type(c))

while True:
    msg = socket.recv()
    print(msg)
    c.ParseFromString(msg)
    print(str(c))
    print('success')
    print(type(c))
