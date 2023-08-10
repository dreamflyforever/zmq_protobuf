import time

import zmq
import logging
import google.protobuf

#from battery_pb2 import *
from Header_pb2 import *
from CameraBottle2Robot_pb2 import *
from Camera2Robot_pb2 import *
c = CameraBottle2RobotReply()
c.seq = 5
#c.error.flag = 100

basestation = CameraBottle2RobotReply()
basestation.error.flag = 1
#basestation.header = 1
# log file
logging.basicConfig(
    level=logging.DEBUG,  # 指定日志记录级别为DEBUG及以上
    format='%(asctime)s %(levelname)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间戳格式
    filename='server.log',  # 将日志记录输出到文件
    filemode='a'  # 文件模式，如果设置为'a'则表示追加记录而不是覆盖
)

ctx = zmq.Context()
url = 'tcp://*:8003'
server = ctx.socket(zmq.REP)
server.bind(url)

msg = c

recv = Camera2RobotRequest()

while True:
    c.seq = c.seq + 1
    c.error.flag = True
    basestation.seq = basestation.seq + 1
    #basestation.poses.pose.y2 = 2
    #basestation.poses.pose.ts = 3
    
    mark = c.data
    mark.Pack(basestation)


    msg_request = server.recv(copy=False)

    recv.ParseFromString(msg_request)
    print(recv)
    if recv.event == 0:
        print('battery request')
    elif recv.event == 1:
        print('fish eye request')
    else:
        print('error message %s' % msg_request)
    #server.send_string('reply %i' % i, routing_id=msg.routing_id)
    msg.ts = time.time()
    serialized_msg = msg.SerializeToString()
    logging.debug('\n%s', msg)
    print(basestation.seq)
    #print(serialized_msg)
    server.send(serialized_msg)
    time.sleep(0.1)
server.close()
ctx.term()
