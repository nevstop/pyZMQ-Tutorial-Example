import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.bind("tcp://*:7788")

# wait all worker connected
time.sleep(1)

for i in range(9):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print 'Compute %s + %s ...' % (a, b)

    # send request to peer
    socket.send_multipart([str(a), str(b)])

    # receive response from peer
    rep = socket.recv()
    print ' =', rep