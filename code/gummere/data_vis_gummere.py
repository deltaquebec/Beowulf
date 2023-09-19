import pandas as pd
import collections
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import nltk
from nltk import pos_tag

# Load the dataframe
df = pd.read_csv('df_clean_gummere.csv')

# Access the contents of the 'Content' column for the row of index 0
contents = df.iloc[0, df.columns.get_loc('Content')]
#contents = ' '.join(contents)

# Access the contents of the 'Content' column, excluding the row of index 0
avg_word_length = df['Average Word Length']

#########################################################################
# n-gram
#########################################################################
def ngram(text):
    # Tokenize the text into words
    words = text.split()
    
    # Extract the monograms, bigrams, and trigrams from the text
    monograms = words
    bigrams = [words[i] + " " + words[i+1] for i in range(len(words)-1)]
    trigrams = [words[i] + " " + words[i+1] + " " + words[i+2] for i in range(len(words)-2)]

    # Compute the frequency of each monogram, bigram, and trigram
    monogram_freq = collections.Counter(monograms)
    bigram_freq = collections.Counter(bigrams)
    trigram_freq = collections.Counter(trigrams)

    # Sort the monograms, bigrams, and trigrams by their frequency
    sorted_monograms = sorted(monogram_freq, key=monogram_freq.get, reverse=True)
    sorted_bigrams = sorted(bigram_freq, key=bigram_freq.get, reverse=True)
    sorted_trigrams = sorted(trigram_freq, key=trigram_freq.get, reverse=True)

    # Select the top 10 most frequent monograms, bigrams, and trigrams
    top_monograms = sorted_monograms[:10]
    top_bigrams = sorted_bigrams[:10]
    top_trigrams = sorted_trigrams[:10]

    # Visualize the frequency of the top 10 most frequent monograms, bigrams, and trigrams
    plt.figure()

    plt.subplot(311)
    plt.bar(range(len(top_monograms)), [monogram_freq[m] for m in top_monograms])
    plt.xticks(range(len(top_monograms)), top_monograms)
    plt.title('Top 10 most frequent monograms')

    plt.subplot(312)
    plt.bar(range(len(top_bigrams)), [bigram_freq[b] for b in top_bigrams])
    plt.xticks(range(len(top_bigrams)), top_bigrams)
    plt.title('Top 10 most frequent bigrams')

    plt.subplot(313)
    plt.bar(range(len(top_trigrams)), [trigram_freq[t] for t in top_trigrams])
    plt.xticks(range(len(top_trigrams)), top_trigrams)
    plt.title('Top 10 most frequent trigrams')

    plt.tight_layout()

    plt.savefig("vis_data_grams.png", dpi=300)
    plt.show()

ngram(contents)

#########################################################################
# wordcloud
#########################################################################
def cloud(text):
    # Create a wordcloud from the contents of the 'Content' column
    wordcloud = WordCloud().generate(contents)

    # Display the wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    plt.savefig("vis_data_cloud.png", dpi=300)
    plt.show()

cloud(contents)

#########################################################################
# Prob density of avergae word length
#########################################################################
def leng(text):
    f = plt.figure()

    # Plot the probability density of the average word length
    #sns.histplot(avg_word_length, stat='density', kde=True, color='blue')
    
    # Plot the probability density of the average word length
    avg_word_length.plot.kde()

    plt.title("Average Word Length in Poem")
    plt.xlabel("Average Word Length")
    plt.ylabel("Probability Density")

    plt.savefig("vis_data_leng.png", dpi=300)
    plt.show()

leng(avg_word_length)

#########################################################################
# POS distributions
#########################################################################
def pos_macro(text):
    # Split the text into a list of words
    words = text.split()

    # Tag the words with their parts of speech
    tagged_words = pos_tag(words)

    # Count the number of each type of part of speech in the text
    n_count = 0
    jj_count = 0
    v_count = 0
    for word, pos in tagged_words:
        if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS":
            n_count += 1
        elif pos == "JJ" or pos == "JJR" or pos == "JJS":
            jj_count += 1
        elif pos == "VB" or pos == "VBD" or pos == "VBG" or pos == "VBN" or pos == "VBP" or pos == "VBZ":
            v_count += 1

    # Create a bar chart showing the number of each type of part of speech
    x = ["Nouns", "Adjectives", "Verbs"]
    y = [n_count, jj_count, v_count]
    plt.bar(x, y)

    # Add labels and title to the plot
    plt.xlabel("Part of Speech")
    plt.ylabel("Frequency")
    plt.title("Number of Parts of Speech in Text")

    # Show the plot
    plt.savefig("vis_data_macro.png", dpi=300)
    plt.show()

pos_macro(contents)

#########################################################################
# POS distributions
#########################################################################
def pos_micro(text):
    # Split the text into a list of words
    words = text.split()

    # Tag the words with their parts of speech
    tagged_words = pos_tag(words)

    # Count the number of each type of part of speech in the text
    nn_count = 0
    nns_count = 0
    nnp_count = 0
    nnps_count = 0
    jj_count = 0
    jjr_count = 0
    jjs_count = 0
    vb_count = 0
    vbd_count = 0
    vbg_count = 0
    vbn_count = 0
    vbp_count = 0
    vbz_count = 0
    for word, pos in tagged_words:
        if pos == "NN":
            nn_count += 1
        elif pos == "NNS":
            nns_count += 1
        elif pos == "NNP":
            nnp_count += 1
        elif pos == "NNPS":
            nnps_count += 1
        elif pos == "JJ":
            jj_count += 1
        elif pos == "JJR":
            jjr_count += 1
        elif pos == "JJS":
            jjs_count += 1
        elif pos == "VB":
            vb_count += 1
        elif pos == "VBD":
            vbd_count += 1
        elif pos == "VBG":
            vbg_count += 1
        elif pos == "VBN":
            vbn_count += 1
        elif pos == "VBP":
            vbp_count += 1
        elif pos == "VBZ":
            vbz_count += 1

    # Create a bar chart showing the number of each type of part of speech
    x = ["NN", "NNS", "NNP", "NNPS", "JJ", "JJR", "JJS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
    y = [nn_count, nns_count, nnp_count, nnps_count, jj_count, jjr_count, jjs_count, vb_count, vbd_count, vbg_count, vbn_count, vbp_count, vbz_count]
    plt.bar(x, y)

    # Add labels and title to the plot
    plt.xlabel("Part of Speech")
    plt.ylabel("Frequency")
    plt.title("Number of Parts of Speech in Text")

    # Show the plot
    plt.savefig("vis_data_micro.png", dpi=300)
    plt.show()

pos_micro(contents)
