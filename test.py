import os
import json
import pandas as pd

from bangla_dictionary.script.bangla_dictionary import BanglaDictionary
from bangla_dictionary.script.preprocess import rename_columns, fill_null_with_previous_word
from bangla_dictionary.script.read_pickle import get_dict
from bangla_dictionary.script.translator import translate_bengali_to_english
from bangla_dictionary.script.write_pickle import write_to_pickle


# Steps to be followed:
#
#   1. First use the do function to preprocess the xlsx file - it will rename columns and write a csv file and
#      pickle file data
#   2. Secondly, you can use read_or_write_pickle function to read or write pickle file separately
#   3. Then testing function will be used to check the pypi module.
#   4. User also can check translator function to translate bangla list of words into english


# preprocessing xlsx file to proper formatted data
def do():
    filename = os.path.join("bangla_dictionary/data/demo_data.xlsx")
    new_column_names = ["pageNo", "word", "number", "pronunciation", "meaning",
                        "pos", "IPA [B]", "language", "class", "sentence", "source"]

    dataframe = rename_columns(filename, new_column_names)

    # df = pd.DataFrame(dataframe)
    df = fill_null_with_previous_word(df=dataframe)
    df.to_csv("bangla_dictionary/data/demo_data.csv")
    df.to_pickle("bangla_dictionary/data/dict_pkl")


# read or write pickled data separately
def read_or_write_pickle():
    write_pickle = write_to_pickle()
    read_pickle = get_dict()
    print(read_pickle)


# pypi module testing using the proper formatted data
def testing():
    test = BanglaDictionary()
    meaning = test.get_multiple_meanings("অই", "অক্ষিলোম", "অক্ষিপটল", "অংশ")
    meaning2 = test.get_meaning("অই")
    print(meaning)
    print(meaning2)


# Google Translation of Bengali Words
def translator():
    res = {
        "custom_message": "This is a basic translator.",
        "google_translator_message": "Using Google Translator",
        # use list of bangla words as input
        "translation": translate_bengali_to_english(["অকম্পনীয়", "অকর্মা", "অকালপক্ব", "অংশ"]),

    }

    response = json.dumps(res, ensure_ascii=False, indent=4)
    print(response)


if __name__ == "__main__":
    """
    Here all the functions are commented because each of the functions do individual tasks. 
    So while needed just uncomment them before using.
    
    """
    # preprocess the dataset and write csv as well as pickle file
    # do()

    # write pickled data
    # read_or_write_pickle()

    # module testing
    # testing()

    # translates into english using google translator
    # translator()
