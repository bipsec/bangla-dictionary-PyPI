from googletrans import Translator
import json


def translate_bengali_to_english(bengali_words):
    translator = Translator()
    translations = {}

    for word in bengali_words:
        translated = translator.translate(word, src='bn', dest='en')
        translations[word] = translated.text

    return translations


# bengali_words = input("Enter Bengali words separated by commas: ").split(',')
# bengali_words = [word.strip() for word in bengali_words]

# res = {
#     "custom_output": "This is a basic translator.",
#     "google_translator_message": "Using Google Translator",
#     "other_data": translate_bengali_to_english(["অই", "অক্ষিলোম", "অক্ষিপটল", "অংশ"])
# }
#
# # translations = translate_bengali_to_english(["অই", "অক্ষিলোম", "অক্ষিপটল", "অংশ"])
#
# response = json.dumps(res, ensure_ascii=False, indent=4)
# print(response)

# english_translation = translate_bengali_to_english("অংশ")
# print(f"English translation: {english_translation}")
