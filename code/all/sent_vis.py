import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# get the data 
sent_df=pd.read_csv(r'sentiment_scores_all.csv')
# Name sections
section_labels = ['Full text', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
sent_df['section_labels'] = section_labels

#########################################################################
# report statistical scores
#########################################################################
def avgs():
    # txt file for report
    with open("results_sent.txt", "w+") as h:
        print('Statistical Results',file=h)
        print('\n',file=h)

        # VADER results
        print('VADER',file=h)
        print(sent_df[['neg','neu','pos','compound']].describe().apply(lambda x: round(x, 2)),file=h)
        print('\n',file=h)
        
        # TextBLOB results
        print('TextBLOB',file=h)
        print(sent_df[['polarity','subjectivity']].describe().apply(lambda x: round(x, 2)),file=h)
        print('\n',file=h)
        
        # NRC results
        print('NRC',file=h)
        print(sent_df[['fear','anger','anticipation','trust','surprise',
                       'positive','negative','sadness','disgust','joy']].describe().apply(lambda x: round(x, 2)),file=h)
        print('\n',file=h)

avgs()

#########################################################################
# visualize sentament via VADER
#########################################################################
def vader_sent():
    # define plot
    ax = plt.gca()
    # plot relevant data for each neg, neu, and pos
    sent_df.plot(kind='line',x='section_labels', y='neg', color='red', alpha=.35, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='neu', color='blue', alpha=.35, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='pos', color='green', alpha=.35, linewidth=5, ax=ax)
    # set center line
    plt.axhline(y=0, xmin=0, xmax=1, alpha=.5, color='black', linestyle='--', linewidth=5)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Sentiment by Section (VADER)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    plt.ylim(-1,1)
    # axis labels
    plt.xlabel('Section')
    # x-axis annotation
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label
    plt.ylabel('Average Sentiment')
    # show graph
    plt.savefig("vis_sent_vader.png", dpi=300)
    plt.show()

vader_sent()

#########################################################################
# sentiment via TextBLOB
#########################################################################
def blobpol():
    # define plot
    ax2 = plt.gca()
    # plot relevant data for polarity and subjectivity
    sent_df.plot(kind='line',x='section_labels', y='polarity', color='blue', alpha=.35,linewidth=5, ax=ax2)
    sent_df.plot(kind='line',x='section_labels', y='subjectivity', color='orange', alpha=.35, linewidth=5, ax=ax2)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Polarity/Subjectivity by Section (TextBlob)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label
    plt.ylabel('Average Sentiment')
    # show graph
    plt.savefig("vis_sent_blob.png", dpi=300)
    plt.show()

blobpol()

#########################################################################
# polarity sentiment via NRC
#########################################################################
def chapsent():
    # define plot
    ax = plt.gca()
    # plot relevant data for positive and negative sentiment
    sent_df.plot(kind='line',x='section_labels', y='positive', color='green', alpha=.35, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='negative', color='red', alpha=.35, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Sentiment by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc.png", dpi=300)
    plt.show()

chapsent()

#########################################################################
# negativity sentiment via NRC
#########################################################################
def chapneg():
    # define plot
    ax = plt.gca()
    # plot relevant data for negative sentiment
    sent_df.plot(kind='line',x='section_labels', y='anger', color='red', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='disgust', color='purple', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='fear', color='maroon', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='sadness', color='black', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Sentiment (Negative) by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_neg.png", dpi=300)
    plt.show()

chapneg()

#########################################################################
# positivity sentiment via NRC
#########################################################################
def chappos():
    # define plot
    ax = plt.gca()
    # plot relevant data for positive sentiment
    sent_df.plot(kind='line',x='section_labels', y='anticipation', color='blue', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='joy', color='orange', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='surprise', color='lightblue', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='trust', color='green', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Sentiment (Positive) by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_pos.png", dpi=300)
    plt.show()

chappos()

#########################################################################
# diametric sadness/joy via NRC
######################################################################### 
def sadjoy():
    # define plot
    ax = plt.gca()
    # plot relevant data for positive sentiment
    sent_df.plot(kind='line',x='section_labels', y='sadness', color='blue', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='joy', color='yellow', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Joy/Sadness by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_sadjoy.png", dpi=300)
    plt.show()

sadjoy()

#########################################################################
# diametric surprise/anticipation via NRC
#########################################################################    
def surant():
    # define plot
    ax = plt.gca()
    # plot relevant data for surprise/anticipation sentiment
    sent_df.plot(kind='line',x='section_labels', y='anticipation', color='orange', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='surprise', color='teal', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Surprise/Anticipation by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_surant.png", dpi=300)
    plt.show()

surant()

#########################################################################
# diametric trust/disgust via NRC
#########################################################################     
def trudis():
    # define plot
    ax = plt.gca()
    # plot relevant data for trust/disgust sentiment
    sent_df.plot(kind='line',x='section_labels', y='trust', color='green', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='disgust', color='purple', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Trust/Disgust by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_trudis.png", dpi=300)
    plt.show()

trudis()

#########################################################################
# diametric anger/fear via NRC
######################################################################### 
def feang():
    # define plot
    ax = plt.gca()
    # plot relevant data for trust/disgust sentiment
    sent_df.plot(kind='line',x='section_labels', y='anger', color='red', alpha=.45, linewidth=5, ax=ax)
    sent_df.plot(kind='line',x='section_labels', y='fear', color='forestgreen', alpha=.45, linewidth=5, ax=ax)
    # set legend
    plt.legend(loc='best')
    # set title
    plt.title('Anger/Fear by Section (NRC)')
    # axis limits
    plt.xlim(-1,len(sent_df))
    # x-axis label and annotation
    plt.xlabel('Section')
    plt.xticks(np.arange(len(sent_df)), np.arange(len(sent_df)))
    # y-axis label and annotation
    plt.yticks()
    plt.ylabel('Sentiment Score')
    # show graph
    plt.savefig("vis_sent_nrc_feang.png", dpi=300)
    plt.show()

feang()
