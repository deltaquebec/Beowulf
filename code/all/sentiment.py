import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from textblob import TextBlob
from nrclex import NRCLex

#########################################################################
# VADER
#########################################################################
def vader_sentiment(df):
    # Define analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Create an empty list to store the results
    results = []

    # Access the contents of the 'Content' column, starting from the second row
    content = df['Content']

    # Loop through the rows of the 'Content' column
    for index, row in content.iteritems():
        # Obtain the polarity scores for the current row
        scores = analyzer.polarity_scores(row)

        # Append the scores and the text to the results list
        results.append(scores)

    # Create a dataframe from the results list
    vader_df = pd.DataFrame(results)

    # Save the result dataframe to a CSV file
    #vader_df.to_csv('vader_sentiment_scores.csv', index=False)

    return vader_df

    #print(result_df)

#########################################################################
# TextBLOB
#########################################################################
def textblob_sentiment(df):
    # empty list for saving blobbed sentences
    blobs = []

    # blobbify text such that we may work with textblob
    for i in range(len(df)):
        blobs.append(TextBlob(df.loc[i,'Content']))

    # emtpy lissts to store polarity and subjectivity scores
    blob_polr = []
    blob_subj = []

    # iterate over each blobbed text and get polarity and subjectivity scores therein
    for i in blobs:
        sent = i.sentences
        for j in sent:
            polr = j.sentiment.polarity
            subj = j.sentiment.subjectivity
        blob_polr.append(polr)
        blob_subj.append(subj)

    # put scores into dataframe
    polr_df = pd.DataFrame(blob_polr)  
    subj_df = pd.DataFrame(blob_subj)  
    blob_sent = pd.merge(polr_df, subj_df, left_index=True, right_index=True)

    # rename dataframe columns and merge
    blob_sent = blob_sent.rename(columns={'0_x': "polarity", '0_y': 'subjectivity'})

    # Save the result dataframe to a CSV file
    #blob_sent.to_csv('textblob_sentiment_scores.csv', index=False)

    #print(blob_sent)

    return blob_sent

#########################################################################
# NRC
#########################################################################
def nrc(df):
    # Create an empty list to store the results
    results = []

    # Access the contents of the 'Content' column
    content = df['Content']

    # Loop through the rows of the 'Content' column
    for index, row in content.iteritems():
        # Apply the NRC sentiment analysis to the current row
        emotions = NRCLex(row).affect_frequencies

        # Append the scores and the text to the results list
        results.append(emotions)

    # Create a dataframe from the results list
    nrc_df = pd.DataFrame(results)

    # Remove the 'anticip' column from the dataframe
    nrc_df = nrc_df.drop(['anticip'], axis=1)

    # Save the result dataframe to a CSV file
    #nrc_df.to_csv('nrc_sentiment_scores.csv', index=False)
    
    # Print the result dataframe to screen
    #print(nrc_df)

    return nrc_df

# Load the dataframe
df = pd.read_csv('df_clean_all.csv')
    
# Apply snetiment functions to the dataframe
vader_df = vader_sentiment(df)
textblob_df = textblob_sentiment(df)
nrc_df = nrc(df)

# split scores into distinct entries of dataframe
sent_df = pd.concat([vader_df, textblob_df, nrc_df], axis=1)

# Save the result dataframe to a CSV file
sent_df.to_csv('sentiment_scores_all.csv', index=True)

print(sent_df)
