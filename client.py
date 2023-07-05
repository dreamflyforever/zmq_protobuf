import time
import google.protobuf
from battery_pb2 import *
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

url = 'tcp://10.1.3.24:8004'
client = ctx.socket(zmq.REQ)
client.connect(url)

send_request = Camera2RobotRequest()
send_request.event = 1
send_request.ts = 2
send_request.seq = 3
msg = send_request
serialized_send = msg.SerializeToString()

recv = Camera2RobotReply()

while True:
    client.send(serialized_send)

    reply = client.recv()
    print(reply)

    recv.ParseFromString(reply)
    parse = str(recv)
    print(parse)
    logging.debug(parse)
    time.sleep(0.1)

client.close()
ctx.term()
