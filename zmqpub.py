import zmq
import sys
import google.protobuf
import time

from rgbd_repeat_pb2 import *

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:8003")
c = pose_array()
#c.x1[0] = 1
#c.x2[0] = 2
#c.y1[0] = 3
#c.y2[0] = 4
#c.z1[0] = 5
#c.z2[0] = 6
#c.x1[1] = 1
#c.x2[1] = 2
#c.y1[1] = 3
#c.y2[1] = 4
#c.z1[1] = 5
#c.z2[1] = 6

p = c.pose.add()
p.x1 = 1

p = c.pose.add()
p.x1 = 2

while True:
    msg = c
    serialized_msg = msg.SerializeToString()
    socket.send(serialized_msg)
    time.sleep(1)
