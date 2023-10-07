# import modules

import json
import pathlib

from .ipa import BanglaIPATranslator
from .read_pickle import get_dict

# data path for model
parent_path = pathlib.Path(__file__).absolute().parents[1] / "model"/"ipa_model.pth"


class BanglaDictionary:
    """
        This class is responsible for all the outputs not the people behind this.

        In short:
        - Ask for meaning of a word or multiple words, it works fine.
        - Ask for ipa of a word or multiple words, it works fine.
        - Ask for sentence example of a word or multiple words, it shows example of that word based on availability. Still populating..
        - Ask for root lang of a word or multiple words, it works fine if the root of that word is tagged on the dictionary.
        - Ask for topic model of a word or multiple words, it will work fine in future updates. xD
        - Ask for .... ( why are you so needy, stop asking....)

        Returns:
        - For different inputs it gives the desired result taken from Bangla Dictionary
    """

    def __init__(self):
        self.model_path = parent_path
        self.data = get_dict()

    def get_meaning(self, word):
        try:
            word_data = self.data.loc[self.data["word"] == word, ["number", "meaning"]]
            if word_data.empty:
                return json.dumps({"Word not found in the dictionary."}, ensure_ascii=False)

            word_dict = {}
            for _, row in word_data.iterrows():
                number = row["number"]
                meaning = row["meaning"]
                if number not in word_dict:
                    word_dict[number] = []
                word_dict[number].append(meaning)

            return json.dumps(word_dict, ensure_ascii=False)
        except IndexError:
            return "Word not found in the dictionary."

    def get_multiple_meanings(self, *words):
        if len(words) == 1:
            return self.get_meaning(words[0])

        meanings = {}

        for word in words:
            try:
                meaning = self.get_meaning(word)
                meanings[word] = meaning
            except IndexError:
                meanings[word] = "Word not found in the dictionary."

        return meanings

    def get_ipa(self, word):
        try:
            ipa = BanglaIPATranslator(self.model_path)

            ipa_translated = ipa.translate(word)

            # print(ipa_translated)
            return ipa_translated
        except IndexError:
            return "IPA is not generated from the model"

    def get_multiple_ipa(self, *words):
        if len(words) == 1:
            try:
                return self.get_ipa(words[0])
            except IndexError:
                return "IPA is not generated from the model"

        ipas = {}

        for word in words:
            try:
                ipa = self.get_ipa(word)
                ipas[word] = ipa
            except IndexError:
                ipas[word] = "IPA is not generated from the model"

        return ipas

    def get_root_lang(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "language"].iloc[0]
        except IndexError:
            return "Root Language not found in the dictionary."

    def get_multiple_root_lang(self, *words):
        if len(words) == 1:
            try:
                return self.get_root_lang(words[0])
            except IndexError:
                return "Root Language not found in the dictionary."

        root_langs = {}

        for word in words:
            try:
                root_lang = self.get_root_lang(word)
                root_langs[word] = root_lang
            except IndexError:
                root_langs[word] = "Root Language not found in the dictionary."

        return root_langs

    def get_pronunciation(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "pronunciation"].iloc[0]
        except IndexError:
            return "Pronunciation not found in the dictionary."

    def get_multiple_pronunciations(self, *words):
        if len(words) == 1:
            try:
                return self.get_pronunciation(words[0])
            except IndexError:
                return "Pronunciation not found in the dictionary."

        pronunciations = {}

        for word in words:
            try:
                pronunciation = self.get_pronunciation(word)
                pronunciations[word] = pronunciation
            except IndexError:
                pronunciations[word] = "Pronunciation not found in the dictionary."

        return pronunciations

    def get_example(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "sentence"].iloc[0]
        except IndexError:
            return "Example not found in the dictionary."

    def get_multiple_examples(self, *words):
        if len(words) == 1:
            try:
                return self.get_example(words[0])
            except IndexError:
                return "Example not found in the dictionary."

        examples = {}

        for word in words:
            try:
                example = self.get_example(word)
                examples[word] = example
            except IndexError:
                examples[word] = "Example not found in the dictionary."

        return examples

    def get_pos(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "pos"].iloc[0]
        except IndexError:
            return "POS not found in the dictionary."

    def get_multiple_pos(self, *words):
        if len(words) == 1:
            try:
                return self.get_pos(words[0])
            except IndexError:
                return "POS not found in the dictionary."

        pos_list = {}

        for word in words:
            try:
                pos = self.get_pos(word)
                pos_list[word] = pos
            except IndexError:
                pos_list[word] = "POS not found in the dictionary."

        return pos_list

    def get_type(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "class"].iloc[0]
        except IndexError:
            return "Type not found in the dictionary."

    def get_multiple_types(self, *words):
        if len(words) == 1:
            try:
                return self.get_type(words[0])
            except IndexError:
                return "Type not found in the dictionary."

        types = {}

        for word in words:
            try:
                word_type = self.get_type(word)
                types[word] = word_type
            except IndexError:
                types[word] = "Type not found in the dictionary."

        return types

    def get_source(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "source"].iloc[0]
        except IndexError:
            return "Source not found in the dictionary."

    def get_multiple_sources(self, *words):
        if len(words) == 1:
            try:
                return self.get_source(words[0])
            except IndexError:
                return "Source not found in the dictionary."

        sources = {}

        for word in words:
            try:
                source = self.get_source(word)
                sources[word] = source
            except IndexError:
                sources[word] = "Source not found in the dictionary."

        return sources

# testing

# test = BanglaDictionary()
# test.get_meaning("অক্ষিপুট")
# test.get_ipa("অক্ষিপুট")
