import pandas as pd


def extract_word_to_txt(input_file, output_file, column_name):
    """
        This code blocks writes the all words in a txt file for some important reasons,jeta bola jabe na.
    :Parameters:
        - input path of csv data
        - output file path for writing the txt file ( kutay rakhte chan)
        - oh! which col you want to write into a txt file.
    Returns:
        - xtx file (xD)
    """
    df = pd.read_csv(input_file)

    column_values = df[column_name]
    column_values = column_values.dropna()

    column_values = column_values.str.strip()
    count = 0

    with open(output_file, 'w') as file:
        for value in column_values:
            count += 1
            file.write(str(value) + '\n')

    print("Total Words", count)


# testing

# input_file = "./../data/demo_data.csv"
# output_file = "./../word_details/words.txt"
# column_name = "word"
#
# extract_word_to_txt(input_file, output_file, column_name)
