import zmq
import random

context = zmq.Context()

publisher = context.socket(zmq.PUB)

publisher.bind("tcp://*:5556")
#publisher.bind("ipc://weather.ipc")

while True:
    zipcode = random.randint(0,100000)
    temperature = random.randint(0,215) - 80
    relhumidity = random.randint(0,50) + 10

    print 'zipcode = %s, temperature = %s, relhumidity = %s' % (zipcode, temperature, relhumidity)

    publisher.send_multipart([str(zipcode), str(temperature), str(relhumidity)])