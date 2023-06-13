import requests
import csv
from textblob import TextBlob
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def collect_news_google(query):
    api_key = "<your_API_key_here>"  # replace with your API key
    query = query.replace(" ", "+")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        news_json = response.json()
        articles = news_json["articles"]
        return articles
    else:
        return []


cybersecurity_news = collect_news_google("cybersecurity")
osint_news = collect_news_google("osint")

# Write the cybersecurity news to a .csv file
with open('cybersecurity_news.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'description', 'url', 'publishedAt', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in cybersecurity_news:
        writer.writerow({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'publishedAt': article['publishedAt'],
            'content': article['content']
        })

# Write the osint news to a .csv file
with open('osint_news.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'description', 'url', 'publishedAt', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in osint_news:
        writer.writerow({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'publishedAt': article['publishedAt'],
            'content': article['content']
        })


def get_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment == 0:
        return "neutral"
    else:
        return "negative"


current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Analyze the sentiment of the cybersecurity news
with open("cybersecurity_news.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    with open("cybersecurity_news_sentiment.txt", "a", encoding="utf-8") as txtfile:
        txtfile.write(f"\n\nDate of news collection: {current_date}\n\n")
        for row in reader:
            sentiment = get_sentiment(row["content"])
            txtfile.write(f"Title: {row['title']}\n")
            txtfile.write(f"Sentiment: {sentiment}\n\n")

# Analyze the sentiment of the OSINT news
with open("osint_news.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    with open("osint_news_sentiment.txt", "a", encoding="utf-8") as txtfile:
        txtfile.write(f"\n\nDate of news collection: {current_date}\n\n")
        for row in reader:
            sentiment = get_sentiment(row["content"])
            txtfile.write(f"Title: {row['title']}\n")
            txtfile.write(f"Sentiment: {sentiment}\n\n")


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
plt.ylim(100, 3500)
plt.yticks(np.arange(100, 3500, 500))
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
