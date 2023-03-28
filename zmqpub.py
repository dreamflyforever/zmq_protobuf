import zmq
import sys
import google.protobuf
import time

from test_protobuf_pb2 import *

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:8003")
c = test_data()
c.x1 = 1
c.x2 = 2
c.y1 = 3
c.y2 = 4
c.z1 = 5
c.z2 = 6

while True:
    msg = c
    serialized_msg = msg.SerializeToString()
    socket.send(serialized_msg)
    time.sleep(1)
