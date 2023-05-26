import time

import zmq

ctx = zmq.Context()

url = 'tcp://*:8001'
server = ctx.socket(zmq.REP)
server.bind(url)

for i in range(10):
    msg = server.recv(copy=False)
    #print(f'server recvd {msg.bytes!r} from {msg.routing_id!r}')
    print(msg)
    #server.send_string('reply %i' % i, routing_id=msg.routing_id)
    server.send_string('reply %i' % i)
    time.sleep(0.1)
server.close()
ctx.term()
