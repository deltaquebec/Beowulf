# etymon.py
import ety
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

def classify_language_family(word):
    origins = ety.origins(word)
    germanic_languages = ['ang', 'enm', 'eng', 'non', 'goh', 'gmh', 'osx', 'got']
    romance_languages = ['lat', 'fro', 'frm', 'fra', 'ita', 'spa', 'por', 'ron']
    hellenic_languages = ['grc', 'ell']
    semitic_languages = ['arc', 'heb', 'ara', 'phn', 'syc', 'akk', 'xpu', 'eth']
    celtic_languages = ['gco', 'iri', 'bre', 'cym', 'gla']
    indo_iranian_languages = ['inc', 'hin', 'ben', 'urd', 'fas', 'pan', 'guj', 'nep', 'sin']
    turkic_languages = ['tur', 'aze', 'tuk', 'uig']
    uralic_languages = ['fin', 'est', 'hun']
    
    for origin in origins:
        if origin.language.iso in germanic_languages:
            return 'Germ.'
        if origin.language.iso in romance_languages:
            return 'Lat.'
        if origin.language.iso in hellenic_languages:
            return 'Hell.'
        if origin.language.iso in semitic_languages:
            return 'Sem.'
        if origin.language.iso in celtic_languages:
            return 'Celt.'
        if origin.language.iso in indo_iranian_languages:
            return 'Indo-Iran.'
        if origin.language.iso in turkic_languages:
            return 'Turk.'
        if origin.language.iso in uralic_languages:
            return 'Ural.'
    
    return 'Other'

def compute_language_families(df):
    # create a dictionary to store the count of each language family by row
    language_family_counts = {}
    
    # iterate over the rows of the dataframe
    for index, row in df.iterrows():
        # split the row's 'Content' field into a list of words
        words = row['Unique Content'].split()
        # create an empty dictionary to store the count of each language family for this row
        row_language_counts = {'Germ.': 0, 'Lat.': 0, 'Hell.': 0, 'Sem.': 0, 'Celt.': 0, 'Indo-Iran.': 0, 'Turk.': 0, 'Ural.': 0, 'Other': 0}
        # iterate over the words
        for word in words:
            # classify the word's language family
            language_family = classify_language_family(word.lower())
            # increment the count for this language family in the row's dictionary
            row_language_counts[language_family] += 1
        # add the row's dictionary of language family counts to the overall dictionary
        language_family_counts[index] = row_language_counts

    # create a dictionary to store the percentage and counts of each language family by row
    language_family_info = {}
    
    # iterate over the rows of the dataframe
    for index, row_language_counts in language_family_counts.items():
        # compute the total number of words in the row
        total_words = sum(row_language_counts.values())
        
        # create a dictionary to store the percentage and counts of each language family for this row
        row_language_info = {}
        
        # compute the percentage and count of each language family for this row
        for language_family, count in row_language_counts.items():
            percentage = count / total_words * 100
            row_language_info[language_family] = {'percentage': percentage, 'count': count}
        
        # add the row's dictionary of language family percentages to the overall dictionary
        language_family_info[index] = row_language_info
    
    # write the language family percentages and counts to a file
    with open('language_family_info.txt', 'w') as f:
        for row, language_family_info in language_family_info.items():
            f.write('Row {}: '.format(row))
            for language_family, info in language_family_info.items():
                f.write('{}: {:.2f}% ({})  '.format(language_family, info['percentage'], info['count']))
            f.write('\n')


def plot_language_families_stack(df):
    # create an empty dictionary to store the count of each language family by row
    language_family_counts = {}
    
    # iterate over the rows of the dataframe
    for index, row in df.iterrows():
        # split the row's 'Content' field into a list of words
        words = row['Unique Content'].split()
        # create an empty dictionary to store the count of each language family for this row
        row_language_counts = {'Germ.': 0, 'Lat.': 0, 'Hell.': 0, 'Sem.': 0, 'Celt.': 0, 'Indo-Iran.': 0, 'Turk.': 0, 'Ural.': 0, 'Other': 0}
        # iterate over the words
        for word in words:
            # classify the word's language family
            language_family = classify_language_family(word.lower())
            # increment the count for this language family in the row's dictionary
            row_language_counts[language_family] += 1
        # add the row's dictionary of language family counts to the overall dictionary
        language_family_counts[index] = row_language_counts
    
    # create a figure and axes object
    fig, ax = plt.subplots()
    
    # iterate over the rows in the language family counts dictionary
    for row, language_count_dict in language_family_counts.items():
        # extract the counts for each language family for this row
        counts = list(language_count_dict.values())
        # plot the counts as a stacked bar chart
        ax.bar(row, counts[0], color='tab:blue')
        ax.bar(row, counts[1], bottom=counts[0], color='tab:orange')
        ax.bar(row, counts[2], bottom=sum(counts[:2]), color='tab:green')
        ax.bar(row, counts[3], bottom=sum(counts[:3]), color='tab:red')
        ax.bar(row, counts[4], bottom=sum(counts[:4]), color='tab:purple')
        ax.bar(row, counts[5], bottom=sum(counts[:5]), color='tab:brown')
        ax.bar(row, counts[6], bottom=sum(counts[:6]), color='tab:pink')
        ax.bar(row, counts[7], bottom=sum(counts[:7]), color='tab:gray')
        ax.bar(row, counts[8], bottom=sum(counts[:8]), color='tab:olive')
    
    # add labels and title
    ax.set_ylabel('Count')
    ax.set_title('Language Family Counts by Row')
    
    # create a legend
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k") for c in ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive']]
    labels = ['Germ.', 'Lat.', 'Hell.', 'Sem.', 'Celt.', 'Indo-Iran.', 'Turk.', 'Ural.', 'Other']
    ax.legend(handles, labels)
    
    # show the plot
    plt.show()


def plot_language_families(df):
    # create an empty dictionary to store the count of each language family by row
    language_family_counts = {}

    # iterate over the rows of the dataframe
    for index, row in df.iterrows():
        # split the row's 'Content' field into a list of words
        words = row['Unique Content'].split()
        # create an empty dictionary to store the count of each language family for this row
        row_language_counts = {'Germ.': 0, 'Lat.': 0, 'Hell.': 0, 'Sem.': 0, 'Celt.': 0, 'Indo-Iran.': 0, 'Turk.': 0, 'Ural.': 0, 'Other': 0}
        # iterate over the words
        for word in words:
            # classify the word's language family
            language_family = classify_language_family(word.lower())
            # increment the count for this language family in the row's dictionary
            row_language_counts[language_family] += 1
        # add the row's dictionary of language family counts to the overall dictionary
        language_family_counts[index] = row_language_counts

    # create a figure and axes object
    fig, ax = plt.subplots()

    # create a list of the language family keys to use for the x-axis
    language_families = ['Germ.', 'Lat.', 'Hell.', 'Sem.', 'Celt.', 'Indo-Iran.', 'Turk.', 'Ural.', 'Other']

    # create a list of colors to use for the bars
    colors = ['#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#56B4E9', '#E69F00', '#CC99CC', '#999999']

    # iterate over the rows in the language family counts dictionary
    for row, language_count_dict in language_family_counts.items():
        # extract the counts for each language family for this row
        counts = list(language_count_dict.values())
        # create a list of x-axis positions for each bar
        positions = [language_families.index(language_family) + row * (len(language_families) + 1) for language_family in language_families]
        # plot the counts as a stacked bar chart
        ax.bar(positions, counts, color=colors, width=0.8)

    # set the x-axis tick positions and labels
    ax.set_xticks([row * (len(language_families) + 1) + len(language_families) / 2 for row in range(len(df))])
    ax.set_xticklabels(df['Filename'], rotation=90)

    # add labels and title
    ax.set_ylabel('Count')
    ax.set_title('Language Family Counts by Row')

    # create a legend
    handles = [plt.Rectangle((0, 0), 1, 1, color=c, ec="k") for c in colors]
    labels = language_families
    ax.legend(handles, labels)

    # show the plot
    plt.show()

def write_other_words(df):
    # create a list to store the words classified under "Other" language family
    other_words = []
    
    # iterate over the rows of the dataframe
    for index, row in df.iterrows():
        # split the row's 'Content' field into a list of words
        words = row['Unique Content'].split()
        # iterate over the words
        for word in words:
            # classify the word's language family
            language_family = classify_language_family(word.lower())
            # if the language family is "Other", add the word to the list
            if language_family == "Other":
                other_words.append(word)

    # write the other words to a file
    with open('other_words.txt', 'w', encoding='utf-8') as f:
        for word in other_words:
            f.write('{}\n'.format(word))


df = pd.read_csv("df_clean_oe.csv")
plot_language_families_stack(df)
plot_language_families(df)
compute_language_families(df)
write_other_words(df)
