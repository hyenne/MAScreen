# from googletrans import Translator
# translator = Translator()
# result = translator.translate('안녕하세요.', dest="ja")
# # print(result[0].text)
# print(result)

# from google.cloud import translate_v2 as translate

# client = translate.Client()
# result = client.translate('How are you?', target_language='ja')
# print(result['translatedText'])

"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
from google.cloud import translate_v2 as translate
translate_client = translate.Client()

# if isinstance(text, six.binary_type):
#     text = text.decode('utf-8')

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(
    "hi", target_language="fr")

print(u'Text: {}'.format(result['input']))
print(u'Translation: {}'.format(result['translatedText']))
print(u'Detected source language: {}'.format(
    result['detectedSourceLanguage']))