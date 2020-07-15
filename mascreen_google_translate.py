from google.cloud import translate

def translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID"):
    """Translating Text."""
    translated_result = ''

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code="fr",
    )
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
        translate_result += translation.translated_text
    return translated_result


def main():
    f= open("./stt_reader/result/stt.txt","r")
    temp = text
    text = f.read()
    if temp == text:
        time.sleep(1)
        print ('Nothing New')
    else:
        transcript = translate_text(text, "mascreen")
        f= open("./stt/result/translated.txt","w")
        f.write(transcript)
        f.close()
        