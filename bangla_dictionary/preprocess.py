import os
import pandas as pd

filename = os.path.join("/home/bip/PycharmProjects/pythonProject/Dictionary/data/demo_data.xlsx")


def rename_columns(file, new_column_name):
    # read the Excel file
    df = pd.read_excel(file)
    df = df.drop(['Unnamed: 11',
                  'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
                  'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
                  'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'PoS',
                  'ভাষা বিষয়ক.1', 'বিষয়-নির্দেশক.1'], axis=1, inplace=True)

    # rename all the columns with a new list of column name
    df.columns = new_column_name

    return df


new_column_names = ["pageNo", "word", "spelling", "pronunciation", "meaning",
                    "pos", "IPA [B]", "language", "class", "sentence", "source"]

dataframe = rename_columns(filename, new_column_names)

df = pd.read_excel(dataframe)

print(df)
