from sklearn.svm import SVC
import joblib
import serial
import keyboard
import util
import zerorpc
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename="./logs_emotion.txt")

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

ledTable = {}
for i in range(11):
    ledTable[i] = util.fileToLEDString("./led/emotion/{}.txt".format(i))

numVals = range(0,9)
output = [0,0,0,0,0,0,0,0,0]
vals = [0,0,0,0,0,0,0,0,0]
init = [0,0,0,0,0,0,0,0,0]
flags = [0xff, 0xfe, 0xfd, 0xfc, 0xfb, 0xfa, 0xef, 0xee, 0xed]
svc = joblib.load("./checkpoints/model_emotion.pkl")
size=100
was_pressed = False

last = int(round(time.time() * 1000))
interval = 120
lastData = -1

port = serial.Serial(
    port='COM3', 
    baudrate=9600,
)
def getY(val):
    result = val/1023.0*100
    return int(result)

def sendData(num):
    global last, interval, ledTable, client, lastData
    now = int(round(time.time() * 1000))
    # logging.info("PREDICT: {}".format(num))
    # print("PREDICT: {}".format(num))
    if now - last > interval:
        if lastData == -1 or num != lastData:
            # logging.info("SEND: {}".format(num))
            client.draw(ledTable[num])
            last = now
            lastData = num

sendData(11)
