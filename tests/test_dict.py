import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.test_config import get_test_data_path
from bangla_dictionary.dictionary.bangla_dictionary import BanglaDictionary


class TestBanglaDictionary(unittest.TestCase):
    def setUp(self):
        self.test = BanglaDictionary()
        self.test_data_filename = get_test_data_path()

    def test_get_meanings(self):
        meaning = self.test.get_meaning("মহারাজ")
        self.assertIsNotNone(meaning)

    def test_get_multiple_meanings(self):
        multiple_meaning = self.test.get_multiple_meanings("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি",
                                                           "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_meaning)

    def test_get_ipa(self):
        ipa = self.test.get_ipa("ভারকেন্দ্র")
        self.assertIsNotNone(ipa)

    def test_get_multiple_ipa(self):
        ipa2 = self.test.get_multiple_ipa("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
        self.assertIsNotNone(ipa2)

    def test_get_pos(self):
        pos = self.test.get_pos("")
        self.assertIsNotNone(pos)

    def test_get_multiple_pos(self):
        multiple_pos = self.test.get_multiple_pos("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_pos)

    def test_get_root_lang(self):
        # Test Language checking functions
        lang = self.test.get_root_lang("খাতকি")
        self.assertIsNotNone(lang)

    def test_get_meanings_root_lang(self):
        lang2 = self.test.get_multiple_root_lang("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
        self.assertIsNotNone(lang2)

    def test_get_pronunciation(self):
        # Test Pronunciation checking functions
        proc = self.test.get_pronunciation("ভারকেন্দ্র")
        self.assertIsNotNone(proc)

    def test_get_meanings_pronunciation(self):
        multiple_proc = self.test.get_multiple_pronunciations("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি",
                                                              "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_proc)

    def test_get_example(self):
        # Test Examples checking functions
        examples = self.test.get_example("খাতাঞ্জি")
        self.assertIsNotNone(examples)

    def test_get_multiple_examples(self):
        multiple_examples = self.test.get_multiple_examples("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি",
                                                            "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_examples)

    def test_get_type(self):
        type_result = self.test.get_type("সম্প্রতি")
        self.assertIsNotNone(type_result)

    def test_get_multiple_type(self):
        multiple_type = self.test.get_multiple_types("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি",
                                                     "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_type)

    def test_get_source(self):
        # Test Source checking functions
        source = self.test.get_source("ভারকেন্দ্র")
        self.assertIsNotNone(source)

    def test_get_multiple_source(self):
        multiple_source = self.test.get_multiple_sources("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি",
                                                         "ভারকেন্দ্র")
        self.assertIsNotNone(multiple_source)


if __name__ == '__main__':
    unittest.main()

# import os
# import json
# import pandas as pd
#
# from bangla_dictionary.scripts.bangla_dictionary import BanglaDictionary
# from bangla_dictionary.scripts.preprocess import fill_null_with_previous_word
# from bangla_dictionary.scripts.read_pickle import get_dict
# from bangla_dictionary.scripts.translator import translate_bengali_to_english
# from bangla_dictionary.scripts.write_pickle import write_to_pickle
# from bangla_dictionary.scripts.ipa import BanglaIPATranslator
#
#
#





#
# if __name__ == "__main__":
#     """
#     Here all the functions are commented because each of the functions do individual tasks.
#     So while needed just uncomment them before using.
#
#     Steps:
#         - First use the do function to preprocess the xlsx file - it will rename columns and write a csv file and
#             pickle file data
#         - Secondly, you can use read_or_write_pickle function to read or write pickle file separately [Optional]
#         - Then testing function will be used to check the pypi module.
#         - User also can check translator function to translate bangla list of words into english
#     Returns:
#         - Comment out to see the outputs.
#     """
#
#     # preprocess the dataset and write csv as well as pickle file
#     # do()
#
#     # output checking after do function ( mone boro sondeho - kaj korbe ki na -_-)
#     # data = pd.read_csv("path/to/bangla_dictionary.csv")
#     # print(data.shape)
#     # print(data.columns)
#
#     # write pickled data [Optional]
#     # read_or_write_pickle()
#
#     # module testing
#     # testing()
#
#     # translates into english using google translator [Optional]
#     # translator()
#
#     # checking with ipa
#     # ipa_checker("চাষাবাদ")
#
#     # all word to a text file of column ["word"]
#     # input_dir = "path/to/bangla_dictionary.csv"
#     # output_dir = "path/to/output"
#     # extract_word_to_txt(input_file=input_dir, output_file=output_dir, column_name="word")
