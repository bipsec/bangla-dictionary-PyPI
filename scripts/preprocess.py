import pathlib

import pandas as pd

dictionary_data = pathlib.Path(__file__).absolute().parents[2] / "data/bang_dict.xlsx"


def rename_columns(filename, new_column_names):
    """
        What do you think of this code blocks is working for?? - give honest answer...  -_-
        - some shitty works that I don't want to remove. - honest (1)
        - add more...
    """

    try:
        df = pd.read_excel(filename)
        df.drop(['Unnamed: 11',
                 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
                 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
                 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'PoS',
                 'ভাষা বিষয়ক.1', 'বিষয়-নির্দেশক.1'], axis=1, inplace=True)

        df.columns = new_column_names
        return df

    except Exception as e:
        print(f"Error occurred while renaming columns: {e}")


def fill_null_with_previous_word(df):
    df['word'].replace(['', ' '], pd.NA, inplace=True)

    df['pageNo'].fillna(method='ffill', inplace=True)
    df['word'] = df['word'].str.strip()
    df['word'].fillna('', inplace=True)

    value_to_fill_source = "ব্যবহারিক বাংলা অভিধান"
    df['source'] = value_to_fill_source

    return df


#################################################
# filling ipa with ipa
#################################################

def fill_ipa(df1, df2, merge_column, suffix1='', suffix2=''):
    """
    Merge two DataFrames based on a common column.
    Check if it needs to rename the column names

    Parameters:
    - df1: First DataFrame
    - df2: Second DataFrame
    - merge_column: The column used for merging
    - suffix1: Suffix to add to overlapping columns from df1 (default: '')
    - suffix2: Suffix to add to overlapping columns from df2 (default: '')

    Returns:
    - Merged DataFrame
    """

    merged_df = df1.merge(df2, on=merge_column, how='left', suffixes=(suffix1, suffix2))
    return merged_df


###############################################################################
# preprocessing xlsx file to proper formatted data
# this should be done at first to convert the  data into an expected format
#################################################################################
def do(data):
    dataframe = pd.read_excel(data)
    # print(dataframe.columns)
    dataframe.drop(['Unnamed: 0'], axis=1, inplace=True)
    #
    # new_column_names = ["pageNo", "word", "number", "pronunciation", "pos", "IPA",
    #                     "meaning", "language", "class", "sentence", "source"]
    #
    # dataframe.columns = new_column_names
    df = fill_null_with_previous_word(df=dataframe)
    df.to_csv("dictionary/data/dictionary.csv", index=False)
    df.to_pickle("dictionary/data/bangla_dictionary_pkl")
    print("Bangla Dictionary CSV Files and Pickle Files are saved successfully.")

# Testing functions

# csv_file_path = 'path/to/demo_data.csv'
# fill_null_with_previous_word(csv_file_path)
# do(dictionary_data)
