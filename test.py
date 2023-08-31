import os
import pandas as pd

from bangla_dictionary.script.bangla_dictionary import BanglaDictionary
from bangla_dictionary.script.preprocess import rename_columns, fill_null_with_previous_word
from bangla_dictionary.script.read_pickle import get_dict
from bangla_dictionary.script.write_pickle import write_to_pickle


# read the xlsx file and convert it to pickle data

def do():
    filename = os.path.join("bangla_dictionary/data/demo_data.xlsx")
    new_column_names = ["pageNo", "word", "number", "pronunciation", "meaning",
                        "pos", "IPA [B]", "language", "class", "sentence", "source"]

    dataframe = rename_columns(filename, new_column_names)

    # df = pd.DataFrame(dataframe)
    df = fill_null_with_previous_word(df=dataframe)
    df.to_csv("bangla_dictionary/data/demo_data.csv")
    df.to_pickle("bangla_dictionary/data/dict_pkl")


def read_or_write_pickle():
    write_pickle = write_to_pickle()
    read_pickle = get_dict()
    print(read_pickle)


def testing():
    test = BanglaDictionary()
    # meaning = test.get_multiple_root_lang("অই", "অক্ষিলোম", "অক্ষিপটল")
    meaning = test.get_meaning("অই")
    print(meaning)


if __name__ == "__main__":
    # do()
    # read_or_write_pickle()

    # for testing 
    testing()
