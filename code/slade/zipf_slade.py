import matplotlib.pyplot as plt
import string
import nltk
import pandas as pd
from nltk.probability import FreqDist
import numpy as np
from sklearn.linear_model import LinearRegression

def rank_frequency(df):
    # Access the contents of the first row of the 'Content' column
    text = df.loc[0, "Content"]

    # Tokenize the text and calculate the frequency distribution
    tokens = nltk.word_tokenize(text)
    fdist = FreqDist(tokens)

    # Plot the frequency distribution
    fdist.plot(50,cumulative=False)
    plt.show()

def extract_slope(df):
    # Access the contents of the first row of the 'Content' column
    text = df.loc[0, "Content"]

    # Tokenize the text and calculate the frequency distribution
    tokens = nltk.word_tokenize(text)
    fdist = FreqDist(tokens)

    # Get the ranks and frequencies of the tokens
    ranks = np.arange(1, len(fdist)+1)
    freqs = np.array([fdist[token] for token in fdist])

    # Take the log of both the ranks and frequencies
    log_ranks = np.log(ranks)
    log_freqs = np.log(freqs)

    # Fit a line to the log-log plot
    slope, intercept = np.polyfit(log_ranks, log_freqs, 1)
    r_squared = 1 - (sum((log_freqs - (slope * log_ranks + intercept)) ** 2) / ((len(fdist) - 1) * np.var(log_freqs, ddof=1)))

    # Plot the log-log plot and the fitted line
    plt.loglog(ranks, freqs, 'bo', markersize=2)
    plt.plot(np.exp(log_ranks), np.exp(intercept) * np.exp(log_ranks)**slope, 'r-', linewidth=2)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.text(0.65, 0.9, f"Slope: {slope:.4f}\nR^2 Value: {r_squared:.4f}", transform=plt.gca().transAxes)
    plt.show()

    return slope

def extract_slope_no_plot(df):
    # Access the contents of the first row of the 'Content' column
    text = df.loc[0, "Content"]

    # Tokenize the text and calculate the frequency distribution
    tokens = nltk.word_tokenize(text)
    fdist = FreqDist(tokens)
    
    # Get the rank and frequency of each word
    freq_ranks = [(i+1, freq) for i, freq in enumerate(sorted(fdist.values(), reverse=True))]
    
    # Convert ranks and frequencies to numpy arrays
    freq_ranks = np.array(freq_ranks)
    log_freq_ranks = np.log(freq_ranks)

    # Fit a linear regression model to the log-log plot
    X = log_freq_ranks[:, 0].reshape(-1, 1)
    y = log_freq_ranks[:, 1].reshape(-1, 1)
    model = LinearRegression().fit(X, y)

    # Get the slope and R^2 value
    slope = model.coef_[0][0]
    r_squared = model.score(X, y)
    
    print(f"Slope: {slope:.4f}")
    print(f"R^2 Value: {r_squared:.4f}")

# Load the dataframe and select the column with the text
df = pd.read_csv("df_clean_slade.csv")

rank_frequency(df)
extract_slope(df)
extract_slope_no_plot(df)
