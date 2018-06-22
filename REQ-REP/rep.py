import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7788")

print 'Worker %s is running ...' % os.getpid()

while True:
    # receive request
    a, b = socket.recv_multipart()
    a = int(a)
    b = int(b)

    print 'Compute %s + %s and send response' % (a, b)
    socket.send(str(a + b))