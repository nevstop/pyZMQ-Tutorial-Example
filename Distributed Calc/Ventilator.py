import zmq
import random
import time

from zmq import Socket

context = zmq.Context()

# sender is used to sell tasks.
sender = context.socket(zmq.PUSH)  # type: Socket
sender.bind("tcp://*:5557")

# sink is used to start all workers synchronously
sink = context.socket(zmq.PUSH)
sink.connect("tcp://127.0.0.1:5558")

raw_input("Any key down after worker is ready")

sink.send('0')
print 'Start command has been sent'

task_num = 50
total_msec = 0

for i in range(0, task_num):
    workload = 50 # ms random.randint(0,100) + 1
    total_msec += workload
    print 'workload: %d ms' % workload
    sender.send(str(workload))

print 'Estimated time: %d ms' % total_msec

time.sleep(1)
