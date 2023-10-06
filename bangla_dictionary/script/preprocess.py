import pandas as pd

from bangla_dictionary.script.ipa import BanglaIPATranslator

path = "bangla_dictionary/model/ipa_model.pth"

ipa = BanglaIPATranslator(path)


def replace_with_nan(df, values_to_replace):
    for value in values_to_replace:
        try:
            df['word'].replace(value, float('nan'), inplace=True)
        except KeyError:
            print(f"Value '{value}' not found in the 'word' column.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def translate_to_ipa(word):
    try:
        ipa_translated = ipa.translate(word)
        return ipa_translated
    except Exception as e:
        print(f"Error translating '{word}' to IPA: {str(e)}")
        return ""


def fill_null_with_previous_word(df):
    df['word'].replace(['', ' '], pd.NA, inplace=True)

    df['word'].fillna(method='ffill', inplace=True)
    df['pageNo'].fillna(method='ffill', inplace=True)

    df['word'] = df['word'].str.strip()

    df['word'].fillna('', inplace=True)

    value_to_fill_source = "ব্যবহারিক বাংলা অভিধান"
    df['source'] = value_to_fill_source

    return df


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

# Example usage
# csv_file_path = '../data/demo_data.csv'
# fill_null_with_previous_word(csv_file_path)
