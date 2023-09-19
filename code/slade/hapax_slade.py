import pandas as pd
from tqdm import tqdm

def calculate_hapaxes_text(df):
    # create an empty dictionary to store the hapax legomena
    hapaxes = {}

    # iterate over the rows of the dataframe
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        # split the row's 'Content' field into a list of words
        words = row['Content'].split()
        # create an empty set to store the hapax legomena for this row
        row_hapaxes = set()
        # iterate over the words
        for word in words:
            # if the word appears only once in the list, add it to the set
            if words.count(word) == 1:
                row_hapaxes.add(word)
        # add the set of hapax legomena for this row to the dictionary
        hapaxes[index] = row_hapaxes

    # open a file for writing
    with open('hapax_slade.txt', 'w', encoding='utf-8') as f:
        # iterate over the rows in the hapaxes dictionary
        for row, hapax_set in hapaxes.items():
            # write the row number to the file
            f.write(f'Row {row}: ')
            # write the hapax legomena for this row to the file, separated by commas
            f.write(', '.join(hapax_set))
            # add a newline character
            f.write('\n')

def calculate_hapaxes(df):
    # create an empty dictionary to store the hapax legomena
    hapaxes = {}

    # iterate over the rows of the dataframe
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        # split the row's 'Content' field into a list of words
        words = row['Content'].split()
        # create an empty set to store the hapax legomena for this row
        row_hapaxes = set()
        # iterate over the words
        for word in words:
            # if the word appears only once in the list, add it to the set
            if words.count(word) == 1:
                row_hapaxes.add(word)
        # add the set of hapax legomena for this row to the dictionary
        hapaxes[index] = ', '.join(row_hapaxes)

    # create a new DataFrame to store the hapaxes
    hapax_df = pd.DataFrame.from_dict(hapaxes, orient='index', columns=['Hapaxes'])

    return hapax_df

df = pd.read_csv("df_clean_slade.csv")
calculate_hapaxes_text(df)

hapaxes_df = calculate_hapaxes(df)
hapaxes_df.to_csv('hapax_slade.csv', index=False)
