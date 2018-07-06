import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:

    msg = socket.recv()
    print msg

    currentTime = time.time()
    print currentTime

    msg1 = 'client message to server1' + str(currentTime)
    msg2 = 'client message to server2' + str(currentTime)
    socket.send(msg1)
    socket.send(msg2)

    time.sleep(1)