import time
import google.protobuf
from CameraBottle2Robot_pb2 import *
import zmq

ctx = zmq.Context()
import logging

# log file
logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s %(levelname)s: %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='client.log', 
    filemode='a' 
)

url = 'tcp://localhost:8003'
client = ctx.socket(zmq.REQ)
client.connect(url)

send_request = CameraBottle2RobotRequest()
send_request.event = 1
send_request.ts = 2
send_request.seq = 3
msg = send_request
serialized_send = msg.SerializeToString()

recv = CameraBottle2RobotReply()
basestation = FindBottleReply()
while True:
    client.send(serialized_send)

    reply = client.recv()
    #print(reply)

    recv.ParseFromString(reply)
    mark = recv.data
    mark.Unpack(basestation)
    parse = str(recv)
    print(parse)
    logging.debug(parse)
    time.sleep(0.1)

client.close()
ctx.term()
