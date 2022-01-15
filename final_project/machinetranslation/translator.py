# File to convert the string
import json             # for the webpages
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

# now we will authenticate and create the instance of authenticator
myAuthenticator = IAMAuthenticator('3N2TVtN2Vp2BZ7zyO61JoHia28VUWNiTe2Jfpo0qTdPz')
translator_instance = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator=myAuthenticator
)

translator_instance.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/22126147-a43e-4065-bacc-404e541ba6aa')

# now we will make function to convert from english to french
def english_to_french(english_text):
    # code to convert to french, we will use the instance made above, and use its .translate feature
    translation=translator_instance.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

# similarly for the french to english translation
def french_to_english(french_text):
    translation=translator_instance.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
    