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
        'ভাষা বিষয়ক.1', 'বিষয়-নির্দেশক.1'], axis=1,inplace=True)

        # Rename the columns
        df.columns = new_column_names

        return df

    except Exception as e:
        print(f"Error occurred while renaming columns: {e}")



