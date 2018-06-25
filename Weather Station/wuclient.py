import sys
import zmq

print 'Getting weather information'

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
# IPC is not supported on windows
# subscriber.connect("ipc://weather.ipc")

argc = len(sys.argv)

if argc > 1:
    filter = sys.argv[1]
else:
    filter = '10001'

print 'filter =',filter

subscriber.setsockopt(zmq.SUBSCRIBE, filter)

total_temp = 0
iter_num = 10

for i in range(0,iter_num):
    zipcode, temperature, relhumidity = subscriber.recv_multipart()
    zipcode = int(zipcode)
    temperature = int(temperature)
    relhumidity = int(relhumidity)

    print 'zipcode = %s, temperature = %s, relhumidity = %s' % (zipcode, temperature, relhumidity)

    total_temp += temperature

temperature = total_temp/iter_num

print 'zipcode %s average temperature is %s' % (zipcode, temperature)


