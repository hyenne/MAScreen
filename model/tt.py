import zerorpc
import util

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
d = util.fileToLEDString("./led/0.txt")
print(d)
c.draw(d)
