import zmq
import sys
import time

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

receiver.recv_string()

start_time = time.time()

task_nbr = 50

for i in range(0,task_nbr):
    receiver.recv_string()

    if (i/10)*10 == i:
        print ':'
    else:
        print '.'

    sys.stdout.flush()

print 'Using Time: %d ms' %(time.time()-start_time)


