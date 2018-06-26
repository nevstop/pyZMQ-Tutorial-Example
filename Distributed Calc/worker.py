import zmq
import time
import sys

context = zmq.Context()

# receiver is used to get task from task vendor.
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://127.0.0.1:5557")

# worker is used to push result back.
worker = context.socket(zmq.PUSH)
worker.connect("tcp://127.0.0.1:5558")

while(True):
    print 'Waiting for tasks...',

    string = receiver.recv_string()

    print 'sleep for %s ms' % string

    time.sleep((float(string)/1000.0))

    worker.send('1')

    sys.stdout.flush()
