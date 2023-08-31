import pandas as pd


def rename_columns(filename, new_column_names):
    try:
        # Read the Excel file
        df = pd.read_excel(filename)

        # dropping null columns
        df.drop(['Unnamed: 11',
                 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
                 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
                 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'PoS',
                 'ভাষা বিষয়ক.1', 'বিষয়-নির্দেশক.1'], axis=1, inplace=True)

        # Rename the columns
        df.columns = new_column_names
        # df.to_csv('bangla_dictionary/data/demo_data.csv')
        return df

    except Exception as e:
        print(f"Error occurred while renaming columns: {e}")


def replace_with_nan(df, values_to_replace):
    for value in values_to_replace:
        df['word'].replace(value, float('nan'), inplace=True)


def fill_null_with_previous_word(df):
    # Values to be replaced with NaN (null values)
    values_to_replace = ['', ' ']

    # Replace specified values with NaN
    replace_with_nan(df, values_to_replace)

    # Forward fill the null values with the previous word
    df['word'].fillna(method='ffill', inplace=True)

    # Replace remaining NaN values with blank (since only white spaces are considered blank)
    df['word'].fillna('', inplace=True)

    return df

# if __name__ == "__main__":

# Example usage
# csv_file_path = '../data/demo_data.csv'
# fill_null_with_previous_word(csv_file_path)
