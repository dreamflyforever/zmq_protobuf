import time

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

for i in range(10):
    msg = b'request %i' % i
    logging.debug('send : %s ' % msg)
    client.send(msg)
    reply = client.recv_string()
    logging.debug('recv %s' % reply)
    print('client recvd %s' % reply)
    time.sleep(0.1)

client.close()
ctx.term()
