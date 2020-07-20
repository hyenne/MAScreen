import binascii
import zerorpc
import threading
import js2py
js2py.translate_file('renderText.js', 'renderText.py')
from renderText import *
from functools import reduce

import time
import os
import sys

# from google.cloud import texttospeech
# from playsound import playsound

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

data = []
ledTable = []
brokenWords = []

text = ''
def main():
    text=''
    # text_trans = ''
    f_stt = open("./result/stt.txt","w")
    f_stt.write(text)
    f_stt.close()
    while True:
        # filepath = sys.argv[0]
        f_stt= open("./result/stt.txt","r")
        # f_trans= open("./result/translated.txt", "r", encoding="utf-8")
        # f = open(filepath, "r")

        # CHANGE 1ST
        temp = text
        # temp = text_trans
        text = f_stt.read()
        # text_trans = f_trans.read()
        # CHANGE 2ND
        if temp == text:
        # if temp == text_trans:
            time.sleep(0.15)
            # print ('Nothing New')
        else:
            #CHANGE 3RD
            # tts(text, "en-US")
            queue(text)
            # queue(text_trans)
            for i in range(len(brokenWords)):
                data = renderText.renderText(brokenWords[i])
                ledTable = frame(data)
                print (binascii.hexlify(ledTable))
                sendData(ledTable)
                time.sleep(0.15)
            brokenWords.clear()
        f_stt.close()
        # f_trans.close()

def queue(word):
    brokenWords.append(word[0:3])
    if len(word)>3:
        while(len(word)>0):
            if len(word) == 3:
                brokenWords.append(word[1:3])
                brokenWords.append(word[2:3])
                brokenWords.append(word[3:3])
                brokenWords.append('')
                break
            else:
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

def tts(_text, _language) :
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code=_language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("./output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    playsound('output.mp3')

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