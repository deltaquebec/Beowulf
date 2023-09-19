import os
import re
import pandas as pd
import chardet
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

#########################################################################
# raw text
#########################################################################
def raw_df(directory):
    # Create an empty dataframe to store the results
    df_raw = pd.DataFrame(columns=['Filename', 'Number of Words', 'Number of Unique Words', 'Average Word Length', 'Average Sentence Length', 'Content'])

    # Get the list of text files in the current directory
    text_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

    # Go through each text file and count the number of words and unique words
    for file in text_files:
        # Detect the encoding of the text file
        with open(os.path.join(directory, file), "rb") as f:
            data = f.read()
            result = chardet.detect(data)
        with open(os.path.join(directory, file), 'r', encoding=result["encoding"]) as f:
            text = f.read()
            words = text.split()
            num_words = len(words)
            unique_words = set(words)
            num_unique_words = len(unique_words)
            total_length = 0
            for word in words:
                total_length += len(word)
            avg_word_length = total_length / num_words

            sentences = nltk.sent_tokenize(text)
            num_sentences = len(sentences)
            total_sentence_length = 0
            for sentence in sentences:
                total_sentence_length += len(sentence.split())
            avg_sentence_length = total_sentence_length / num_sentences
            avg_words_per_sentence = num_words / num_sentences

            lexical_density = num_unique_words / num_words

        # Add the results to the dataframe
        temp_df = pd.DataFrame({'Filename': [file], 'Number of Words': [num_words], 'Number of Unique Words': [num_unique_words], 'Average Word Length': [avg_word_length], 'Average Sentence Length': [avg_sentence_length], 'Content': [text], 'Average Words per Sentence': [avg_words_per_sentence], 'Lexical Density': [lexical_density]})
        df_raw = pd.concat([df_raw, temp_df], ignore_index=True)
    return df_raw

# test the function
df_raw = raw_df(r"C:\Users\delta\AppData\Local\Programs\Python\Python37\hw\project\all")
# Save the dataframe to a CSV file
df_raw.to_csv('df_raw_all.csv')

print(df_raw)

#########################################################################
# Cleaned text
#########################################################################
def clean_df(directory):
    # Create an empty dataframe to store the results
    df_clean = pd.DataFrame(columns=['Filename', 'Number of Words', 'Number of Unique Words', 'Average Word Length', 'Average Sentence Length', 'Content', 'Unique Content'])

    # Get the list of text files in the current directory
    text_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

    # Go through each text file and count the number of words and unique words
    for file in text_files:
        # Detect the encoding of the text file
        with open(os.path.join(directory, file), "rb") as f:
            data = f.read()
            result = chardet.detect(data)
        with open(os.path.join(directory, file), 'r', encoding=result["encoding"]) as f:
            text = f.read()

            # Clean the text by removing punctuation and lowercasing all words
            text = text.translate(str.maketrans('', '', string.punctuation))
            text = re.sub(r'[^\w\s]', '', text)
            words = [word.lower() for word in text.split()]

            # Remove stopwords from the text
            stop_words = set(stopwords.words('english'))
            modal = ['might','could','should','would','come','came']
            stop_words.update(modal)
            words = [word for word in words if word not in stop_words]

            # lemmatize words
            lemmatizer = WordNetLemmatizer()
            words = [lemmatizer.lemmatize(word) for word in words]

            # Get unique words
            unique_words = list(set(words))

            # Join unique words into a string
            unique_words_string = ' '.join(str(e) for e in unique_words)

            words_clean = ' '.join(str(e) for e in words)

            # Count the number of words and unique words
            num_words = len(words)
            num_unique_words = len(unique_words)

            # Calculate the average word length
            total_length = 0
            for word in words:
                total_length += len(word)
            avg_word_length = total_length / num_words

            # Tokenize the text into sentences and calculate the average sentence length
            sentences = nltk.sent_tokenize(text)
            num_sentences = len(sentences)
            total_sentence_length = 0
            for sentence in sentences:
                total_sentence_length += len(sentence.split())
            avg_sentence_length = total_sentence_length / num_sentences
            avg_words_per_sentence = num_words / num_sentences

            # Calculate the lexical density
            lexical_density = num_unique_words / num_words

        # Add the results to the dataframe
        temp_df = pd.DataFrame({'Filename': [file], 'Number of Words': [num_words],
                                'Number of Unique Words': [num_unique_words], 'Average Word Length': [avg_word_length],
                                'Average Sentence Length': [avg_sentence_length], 'Content': [words_clean],
                                'Unique Content': [unique_words_string], 'List Content': [words],
                                'Average Words per Sentence': [avg_words_per_sentence], 'Lexical Density': [lexical_density]})
        df_clean = pd.concat([df_clean, temp_df], ignore_index=True)
    return df_clean

 # test the function
df_clean = clean_df(r"C:\Users\delta\AppData\Local\Programs\Python\Python37\hw\project\all")
# Save the dataframe to a CSV file
df_clean.to_csv('df_clean_all.csv')

print(df_clean)
