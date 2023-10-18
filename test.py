import os
import json
import pandas as pd

from bangla_dictionary.script.bangla_dictionary import BanglaDictionary
from bangla_dictionary.script.preprocess import fill_null_with_previous_word
from bangla_dictionary.script.read_pickle import get_dict
from bangla_dictionary.script.translator import translate_bengali_to_english
from bangla_dictionary.script.write_pickle import write_to_pickle
from bangla_dictionary.script.ipa import BanglaIPATranslator
from bangla_dictionary.script.words import extract_word_to_txt


def merge_xlsx_files():
    input_dir = os.path.join("bangla_dictionary/data/")
    output_file = os.path.join("bangla_dictionary/data/")
    dataframes = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(input_dir, filename)
            df = pd.read_excel(file_path)
            dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df.to_excel(output_file, index=False)

    print(f"Merged {len(dataframes)} XLSX files into {output_file}")


# preprocessing xlsx file to proper formatted data
def do():
    filename = os.path.join("bangla_dictionary/data/bang_dict.xlsx")

    dataframe = pd.read_excel(filename)
    # print(dataframe.columns)
    dataframe.drop(['Unnamed: 0'], axis=1, inplace=True)
    #
    # new_column_names = ["pageNo", "word", "number", "pronunciation", "pos", "IPA",
    #                     "meaning", "language", "class", "sentence", "source"]
    #
    # dataframe.columns = new_column_names
    df = fill_null_with_previous_word(df=dataframe)
    df.to_csv("bangla_dictionary/data/bangla_dictionary.csv", index=False)
    df.to_pickle("bangla_dictionary/data/bangla_dictionary_pkl")
    print("Bangla Dictionary CSV Files and Pickle Files are saved successfully.")


# read or write pickled data separately
def read_or_write_pickle():
    write_pickle = write_to_pickle()
    read_pickle = get_dict()
    print(read_pickle)


# pypi module testing using the proper formatted data
def testing():
    test = BanglaDictionary()

    # meanings checking functions
    meaning = test.get_meaning("মহারাজ")
    multiple_meaning = test.get_multiple_meanings("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(meaning)
    print(multiple_meaning)
    print("=========================")

    # ipa checking functions
    ipa = test.get_ipa("ভারকেন্দ্র")
    ipa2 = test.get_multiple_ipa("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(ipa)
    print(ipa2)

    print("=========================")

    # pos checking functions
    pos = test.get_pos("খাতাক")
    multiple_pos = test.get_multiple_pos("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(pos)
    print(multiple_pos)

    # lang checking functions
    lang = test.get_root_lang("খাতকি")
    lang2 = test.get_multiple_root_lang("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(lang)
    print(lang2)

    print("=========================")

    # pronunciation checking functions
    proc = test.get_pronunciation("ভারকেন্দ্র")
    multiple_proc = test.get_multiple_pronunciations("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(proc)
    print(multiple_proc)

    print("=========================")

    # examples checking functions
    examples = test.get_example("খাতাঞ্জি")
    multiple_examples = test.get_multiple_examples("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(examples)
    print(multiple_examples)

    print("=========================")

    # pronunciation checking functions
    proc = test.get_pronunciation("চাষাবাদ")
    multiple_proc = test.get_multiple_pronunciations("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(proc)
    print(multiple_proc)

    print("=========================")

    # types checking functions
    type = test.get_type("সম্প্রতি")
    multiple_type = test.get_multiple_types("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(type)
    print(multiple_type)

    print("=========================")

    # source checking functions
    source = test.get_source("ভারকেন্দ্র")
    multiple_source = test.get_multiple_sources("চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র")
    print(source)
    print(multiple_source)


# Google Translation of Bengali Words
def translator():
    res = {
        "custom_message": "This is a basic translator.",
        "google_translator_message": "Using Google Translator",
        # use list of bangla words as input
        "translation": translate_bengali_to_english(["চাষাবাদ", "চিঁহি", "কথায় চিঁড়ে ভেজে না", "সম্প্রতি", "ভারকেন্দ্র"]),

    }

    response = json.dumps(res, ensure_ascii=False, indent=4)
    print(response)


# demo checking with ipa from the model
def ipa_checker(word):
    path = "bangla_dictionary/model/ipa_model.pth"

    ipa = BanglaIPATranslator(path)

    ipa_translated = ipa.translate(word)

    print(ipa_translated)


if __name__ == "__main__":
    """
    Here all the functions are commented because each of the functions do individual tasks. 
    So while needed just uncomment them before using.
    
    Steps:
        - First use the do function to preprocess the xlsx file - it will rename columns and write a csv file and
            pickle file data
        - Secondly, you can use read_or_write_pickle function to read or write pickle file separately [Optional]
        - Then testing function will be used to check the pypi module.
        - User also can check translator function to translate bangla list of words into english
    Returns:
        - Comment out to see the outputs.
    """

    # preprocess the dataset and write csv as well as pickle file
    # do()

    # output checking after do function ( mone boro sondeho - kaj korbe ki na -_-)
    # data = pd.read_csv("path/to/bangla_dictionary.csv")
    # print(data.shape)
    # print(data.columns)

    # write pickled data [Optional]
    # read_or_write_pickle()

    # module testing
    # testing()

    # translates into english using google translator [Optional]
    # translator()

    # checking with ipa
    # ipa_checker("চাষাবাদ")

    # all word to a text file of column ["word"]
    # input_dir = "path/to/bangla_dictionary.csv"
    # output_dir = "path/to/output"
    # extract_word_to_txt(input_file=input_dir, output_file=output_dir, column_name="word")
