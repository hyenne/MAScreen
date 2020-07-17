import binascii
import zerorpc
import threading
import js2py
js2py.translate_file('renderText.js', 'renderText.py')
from renderText import *
from functools import reduce

import time
import os

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

data = []
ledTable = []
brokenWords = []

text = ''
def main():
    text=''
    while True:
        filepath = sys.argv[0]
        # f= open("./result/stt.txt","r")
        f = open(filepath, "r")
        temp = text
        text = f.read()
        if temp == text:
            time.sleep(1)
            print ('Nothing New')
        else:
            queue(text)
            for i in range(len(brokenWords)):
                data = renderText.renderText(brokenWords[i])
                ledTable = frame(data)
                print (binascii.hexlify(ledTable))
                sendData(ledTable)
                time.sleep(1)
            brokenWords.clear()
        f.close()

def queue(word):
    brokenWords.append(word[0:3])
    if len(word) > 3:
        while(len(word)>3):
            word = word[1:]
            brokenWords.append(word[0:3])

def frame(data):
    payload = bytearray(57)
    payload[0] = 0x01
    payload[1] = 0x00
    payload[2] = 0x06
    
    for i in range(0, 54):		
        payload[i + 3] = (data[(i * 4)] >> 6 << 6) | (data[(i * 4) + 1] >> 6 << 4) | (data[(i * 4) + 2] >> 6 << 2) | (data[(i * 4) + 3] >> 6)
    # this._queue(this._encodeMessage(0x03, payload));

    result = encodeMessage(0x03, payload)
    return result

def reducer(p,c):
    return p^c

def encodeMessage(type, payload):
    message = bytearray(len(payload) + 7)
    
    message[0] = 0xfa
    message[1] = type
    message[2] = int(len(payload) / 0xff)
    message[3] = len(payload) % 0xff

    message[4:4+len(payload)] = payload

    message[len(message) - 3] = reduce(reducer, payload)
    message[len(message) - 2] = 0x55
    message[len(message) - 1] = 0xa9
    
    return message
    # 'fa030039010006000ffffff000000bffffe0000007ffffd0000000ffff000000003ffc000000000ff00000000003c000000000000000000000000000003b55a9'

def sendData(leds):
    global client
    client.draw(leds)

# def display():
#     renderText.pos = renderText.pos+1
#     if renderText.pos > renderText.width:
#         renderText.pos = 0
#     renderText.renderText(text)
    
# def setInterval(func,time):
#     e = threading.Event()
#     while not e.wait(time):
#         func()

main()