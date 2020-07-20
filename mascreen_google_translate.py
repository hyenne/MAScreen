from google.cloud import translate_v2 as translate
import sys
import time

# def translate_text(input):
#     client = translate.Client()
#     result = client.translate(input, target_language='ja')
#     print(result['translatedText'])
#     return result

def translate_text(_input_text, _target_language):
    translate_client = translate.Client()

    # if isinstance(text, six.binary_type):
    #     text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(_input_text, target_language=_target_language)

    # print(u'Text: {}'.format(result['input']))
    # print(u'Translation: {}'.format(result['translatedText']))
    # print(u'Detected source language: {}'.format(result['detectedSourceLanguage']))
    return result['translatedText']

def main():
    text=''
    while True:
        f_stt= open("./stt/result/stt.txt","r")
        temp = text
        text = f_stt.read()
        f_stt.close()
        if temp == text:
            time.sleep(0.15)
            print ('Nothing New')
        else:
            transcript = translate_text(text, "it")
            f_trans= open("./stt/result/translated.txt","w", encoding="utf-8")
            # f_trans= open("./stt/result/translated.txt","w")
            f_trans.write(transcript)
            f_trans.close()

main()