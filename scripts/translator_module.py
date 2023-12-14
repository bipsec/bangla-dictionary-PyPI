from googletrans import Translator

def translate_bengali_to_english(bengali_words):
    """
    Translates Bengali words to English using Google Translator.

    Params:
        - bengali_words (list): List of Bengali words to be translated.

    Returns:
        - translations (list): List of English translations corresponding to Bengali words.
    """
    translator = Translator()
    translations = []

    for word in bengali_words:
        translated = translator.translate(word, src='bn', dest='en')
        translations.append(translated.text)

    return translations
