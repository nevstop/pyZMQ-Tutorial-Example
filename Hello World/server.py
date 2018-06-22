import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:7788")

print socket.recv()
socket.send('world')
