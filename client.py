import time
import google.protobuf
from test_protobuf_pb2 import *
import zmq

ctx = zmq.Context()
import logging

# log file
logging.basicConfig(
    level=logging.DEBUG,  # 指定日志记录级别为DEBUG及以上
    format='%(asctime)s %(levelname)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间戳格式
    filename='client.log',  # 将日志记录输出到文件
    filemode='a'  # 文件模式，如果设置为'a'则表示追加记录而不是覆盖
)

url = 'tcp://10.1.9.184:8001'
client = ctx.socket(zmq.REQ)
client.connect(url)

c = test_data()

while True:
    msg = b'request rgbd'
    logging.debug(msg)
    client.send(msg)
    replay = client.recv()
    print(replay)
    c.ParseFromString(replay)
    parse = str(c)
    print(parse)
    logging.debug(parse)
    time.sleep(0.1)

client.close()
ctx.term()
