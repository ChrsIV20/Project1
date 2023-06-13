import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Agg')


# Read the contents of the first .txt file
with open('cybersecurity_news_sentiment.txt', encoding='utf-8') as f:
    file1_contents = f.read()

# Read the contents of the second .txt file
with open('osint_news_sentiment.txt', 'r', encoding='utf-8') as f:
    file2_contents = f.read()


sentiments = ['positive', 'negative', 'neutral']

# Calculate the count of each sentiment in file 1
sentiment_counts_1 = [file1_contents.count(sentiment) for sentiment in sentiments]
print(sentiment_counts_1)

# Calculate the count of each sentiment in file 2
sentiment_counts_2 = [file2_contents.count(sentiment) for sentiment in sentiments]
print(sentiment_counts_2)

# Create a bar chart for the counts in file 1
plt.bar(sentiments, sentiment_counts_1, color='purple', width=0.35)
plt.xlabel('Sentiments')
plt.ylabel('Counts')
plt.ylim(100, 1500)
plt.yticks(np.arange(100, 1500, 200))
plt.title('Cybersecurity News Sentiment Analysis')
plt.savefig('cybersecurity_sentiment.png')
plt.clf()

# Create a bar chart for the counts in file 2
plt.bar(sentiments, sentiment_counts_2, color='purple', width=0.35)
plt.xlabel('Sentiments')
plt.ylabel('Counts')
plt.ylim(100, 3000)
plt.yticks(np.arange(100, 3000, 500))
plt.title('OSINT News Sentiment Analysis')
plt.savefig('osint_sentiment.png')
