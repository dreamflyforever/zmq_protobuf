import time

import zmq
import logging
import google.protobuf

from test_protobuf_pb2 import *
c = test_data()
c.x1 = 1
c.x2 = 2
c.y1 = 3
c.y2 = 4
c.z1 = 5
c.z2 = 6

# log file
logging.basicConfig(
    level=logging.DEBUG,  # 指定日志记录级别为DEBUG及以上
    format='%(asctime)s %(levelname)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间戳格式
    filename='server.log',  # 将日志记录输出到文件
    filemode='a'  # 文件模式，如果设置为'a'则表示追加记录而不是覆盖
)

ctx = zmq.Context()
url = 'tcp://*:8004'
server = ctx.socket(zmq.REP)
server.bind(url)

msg = c

recv = test_data()

while True:
    msg_request = server.recv(copy=False)

    recv.ParseFromString(msg_request)
    logging.debug(recv.cls)
    print(type(recv.cls))
    if recv.cls == 1:
        print('rgbd request')
    elif recv.cls == 0:
        print('fish eye request')
    else:
        print('error message %s' % msg_request)
    #server.send_string('reply %i' % i, routing_id=msg.routing_id)
    msg.ts = time.time()
    serialized_msg = msg.SerializeToString()
    logging.debug('\n%s', msg)
    print(serialized_msg)
    server.send(serialized_msg)
    time.sleep(0.1)
server.close()
ctx.term()
