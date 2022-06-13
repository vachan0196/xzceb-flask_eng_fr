"""Translate functions used by other services
Returns:
    _type_: Translated text
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import machinetranslation

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text: str) ->  str:
    """Translates English input text to French
    Args:
        english_text (str): Input text to be translated
    Returns:
        str: Translated text in French
    """

    if english_text == "":
        return "Nothing to Translate"

    french_text = language_translator.translate(
        text=english_text, model_id='en-fr'
    ).get_result()

    return french_text.get("translations")[0].get('translation')


def french_to_english(french_text: str) -> str:
    """Translates French input text to English
    Args:
        english_text (str): Input text to be translated
    Returns:
        str: Translated text in English
    """

    if french_text == "":
        return "Rien à Translate"

    english_text = language_translator.translate(
        text=french_text, model_id='fr-en'
    ).get_result()

    return english_text.get("translations")[0].get('translation')

print(french_to_english("bonjour"))
