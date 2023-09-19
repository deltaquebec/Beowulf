import pandas as pd

def compare_hapaxes(file_names):
    dfs = []
    for file_name in file_names:
        df = pd.read_csv(file_name)
        df = df.fillna('')
        dfs.append(df)

    # create a dictionary to store the shared and unique hapaxes
    hapaxes_dict = {}

    # iterate over all pairs of dataframes
    for i in range(len(dfs)):
        for j in range(i+1, len(dfs)):
            # iterate over the rows in the dataframes
            for row in range(dfs[0].shape[0]):
                # get the set of hapaxes for the current row in each dataframe
                row_i = set(dfs[i].iloc[row].values[1:].tolist())
                row_j = set(dfs[j].iloc[row].values[1:].tolist())
                # calculate the shared and unique hapaxes
                shared_hapaxes = row_i.intersection(row_j)
                unique_hapaxes_i = row_i.difference(shared_hapaxes)
                unique_hapaxes_j = row_j.difference(shared_hapaxes)
                # add the shared and unique hapaxes to the dictionary
                key = f'{file_names[i]} vs {file_names[j]} - Row {row}'
                hapaxes_dict[key] = {'Shared Hapaxes': shared_hapaxes, 
                                     f'Unique Hapaxes in {file_names[i]}': unique_hapaxes_i, 
                                     f'Unique Hapaxes in {file_names[j]}': unique_hapaxes_j}
                print(key, hapaxes_dict[key])

    # create a dataframe from the dictionary
    result_df = pd.DataFrame.from_dict(hapaxes_dict, orient='index')
    result_df.to_csv('shared_hapaxes.csv', index=False)

    with open('shared_hapaxes.txt', 'w', encoding='utf-8') as f:
        f.write(result_df.to_string(index=False))

    return result_df

file_names = ['hapax_all.csv', 'hapax_gummere.csv', 'hapax_hall.csv', 'hapax_slade.csv']
result_df = compare_hapaxes(file_names)


