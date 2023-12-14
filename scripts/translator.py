import json
import pathlib

from bangla_dictionary.ipa.ipa import BanglaIPATranslator
from .translator_module import translate_bengali_to_english

path = pathlib.Path(__file__).absolute().parents[1] / "model/ipa_model.pth"


def translator():
    """
    Performs translation of Bengali words to English using Google Translator.

    Returns:
        str: JSON-formatted translation response
    """
    res = {
        "custom_message": "This is a basic translator.",
        "google_translator_message": "Using Google Translator",
        # use list of Bengali words as input
        "translation": translate_bengali_to_english(
            ["চাষাবাদ", "সম্প্রতি"])
    }

    return json.dumps(res, ensure_ascii=False, indent=4)



def ipa_checker(word):
    """
    Performs IPA checking with the model.

    Params:
        word (str): Bengali word for IPA checking.

    Returns:
        None
    """
    ipa = BanglaIPATranslator(path)
    ipa_translated = ipa.translate(word)
    print(ipa_translated)
