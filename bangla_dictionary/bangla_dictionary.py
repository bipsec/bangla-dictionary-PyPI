import read_pickle


class BanglaDictionary:
    def __init__(self):
        self.data = read_pickle.get_dict()

    def get_meaning(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "meaning"].iloc[0]
        except IndexError:
            return "Word not found in the dictionary."

    def get_ipa(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "IPA [B]"].iloc[0]
        except IndexError:
            return "IPA not found in the dictionary."

    def get_root_lang(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "language"].iloc[0]
        except IndexError:
            return "Root Language not found in the dictionary."

    def get_pronunciation(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "pronunciation"].iloc[0]
        except IndexError:
            return "Pronunciation not found in the dictionary."

    def get_example(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "sentence"].iloc[0]
        except IndexError:
            return "Example not found in the dictionary."

    def get_pos(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "pos"].iloc[0]
        except IndexError:
            return "POS not found in the dictionary."

    def get_type(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "class"].iloc[0]
        except IndexError:
            return "Type not found in the dictionary."

    def get_source(self, word):
        try:
            return self.data.loc[self.data["word"] == word, "source"].iloc[0]
        except IndexError:
            return "Source not found in the dictionary."
