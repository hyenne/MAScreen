from sklearn.svm import SVC
import joblib
import serial
import keyboard
import util
import zerorpc
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename="./logs2_9600.txt")

# ledTable = {}
# for i in range(12):
#     ledTable[i] = util.fileToLEDString("./led/{}.txt".format(i))

numVals = range(0,9)
output = [0,0,0,0,0,0,0,0,0]
vals = [0,0,0,0,0,0,0,0,0]
init = [0,0,0,0,0,0,0,0,0]
flags = [0xff, 0xfe, 0xfd, 0xfc, 0xfb, 0xfa, 0xef, 0xee, 0xed]
svc = joblib.load("./checkpoints/model_final.pkl")
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

while True:
    if port.readable():
        val=ord(port.read())
        for i in numVals:
            if val==flags[i]:
                value=(ord(port.read())<< 8) | (ord(port.read()))
                vals[i] = value
                output[i]=getY(vals[i])-init[i]
        push=[output]
        preds = svc.predict(push) 
        result=int(preds[0])
        logging.info("PREDICT: {}".format(result))
        # print("PREDICT: {}".format(result))
     
    if keyboard.is_pressed(' '):
        if not was_pressed:
            for i in numVals:
                init[i] = getY(vals[i])
            was_pressed = True
    else:
        was_pressed = False

    # push=[output]
    # preds = svc.predict(push) 
    # result=int(preds[0])
    # logging.info("PREDICT: {}".format(result))
    # print("PREDICT: {}".format(result))
