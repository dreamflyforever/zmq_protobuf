import time

import zmq

ctx = zmq.Context()

url = 'tcp://10.1.9.184:8001'
client = ctx.socket(zmq.REQ)
client.connect(url)

for i in range(10):
    client.send(b'request %i' % i)
    reply = client.recv_string()
    print('client recvd %r' % reply)
    time.sleep(0.1)

client.close()
ctx.term()
