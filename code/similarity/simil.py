import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def simil(df1,df2):
    # Read in the CSV files and extract the relevant text columns
    df_all = pd.read_csv(df1)
    df_gummere = pd.read_csv(df2)
    doc1 = df_all.iloc[0, 6]
    doc2 = df_gummere.iloc[0, 6]

    # Tokenize the documents
    tokens1 = word_tokenize(doc1)
    tokens2 = word_tokenize(doc2)

    # Define the stop words
    stop_words = set(stopwords.words('english'))

    # Remove the stop words and perform stemming
    stemmer = PorterStemmer()
    filtered_tokens1 = [stemmer.stem(word.lower()) for word in tokens1 if word.lower() not in stop_words]
    filtered_tokens2 = [stemmer.stem(word.lower()) for word in tokens2 if word.lower() not in stop_words]

    # Join the stemmed tokens back into a string
    processed_doc1 = " ".join(filtered_tokens1)
    processed_doc2 = " ".join(filtered_tokens2)

    # Create a TF-IDF vectorizer and transform the documents
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([processed_doc1, processed_doc2])

    # Calculate the cosine similarity between the documents
    similarity = cosine_similarity(tfidf[0], tfidf[1])[0][0]

    print(f"Similarities for {df1} {df2}: {round(similarity, 4)}")

dataframes = ['df_clean_all.csv','df_clean_gummere.csv','df_clean_hall.csv','df_clean_slade.csv']

simil('df_clean_all.csv','df_clean_gummere.csv')
simil('df_clean_all.csv','df_clean_hall.csv')
simil('df_clean_all.csv','df_clean_slade.csv')
simil('df_clean_gummere.csv','df_clean_hall.csv')
simil('df_clean_gummere.csv','df_clean_slade.csv')
simil('df_clean_hall.csv','df_clean_slade.csv')

