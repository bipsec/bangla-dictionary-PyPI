import os
import pandas as pd


from preprocess import rename_columns


def do():
    filename = os.path.join("/home/abirhasanmubin/biplab/Dictionary/bangla-dictionary/data/demo_data.xlsx")
    new_column_names = ["pageNo", "word", "spelling", "pronunciation", "meaning",
                    "pos", "IPA [B]", "language", "class", "sentence", "source"]

    dataframe = rename_columns(filename, new_column_names)

    df = pd.DataFrame(dataframe)

    df.to_pickle("dict_pkl")


if __name__ == "__main__":
    do()