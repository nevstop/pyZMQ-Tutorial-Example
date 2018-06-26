import zmq
import sys
import time

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

receiver.recv_string()

start_time = float(time.time())
print 'Start Time: %s' % start_time

task_nbr = 50

for i in range(0,task_nbr):
    receiver.recv_string()

    if (i/10)*10 == i:
        print ':',
    else:
        print '.',

print '/n'

End_time = float(time.time())

print 'End Time: %s' % End_time
print 'Using Time: %d ms' %((End_time - start_time)*1000)


