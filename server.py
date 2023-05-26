import time

import zmq
import logging

# log file
logging.basicConfig(
    level=logging.DEBUG,  # 指定日志记录级别为DEBUG及以上
    format='%(asctime)s %(levelname)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间戳格式
    filename='server.log',  # 将日志记录输出到文件
    filemode='a'  # 文件模式，如果设置为'a'则表示追加记录而不是覆盖
)

ctx = zmq.Context()
url = 'tcp://*:8001'
server = ctx.socket(zmq.REP)
server.bind(url)

for i in range(10):
    msg = server.recv(copy=False)
    #print(f'server recvd {msg.bytes!r} from {msg.routing_id!r}')
    logging.debug('recv %s ' % msg)
    print(msg)
    #server.send_string('reply %i' % i, routing_id=msg.routing_id)
    logging.debug('send %d' % i)
    server.send_string('reply %i' % i)
    time.sleep(0.1)
server.close()
ctx.term()
