import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import re

# Task 1: Scrape all paragraph text from a website of my choice
url = 'https://www.mcsweeneys.net/articles/just-because-im-a-bank-doesnt-mean-im-good-with-money'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
paragraphs = soup.find_all('p')
# Aggregate text from all paragraphs
text = ' '.join([p.text for p in paragraphs])
print(text)

# Task 2: Create or find a list of stop words
stop_words = [
    "a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", "aren", "aren't",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "couldn", "couldn't",
    "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few",
    "for", "from", "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having", "he",
    "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it",
    "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my",
    "myself", "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once", "only", "or", "other", "our",
    "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've",
    "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them",
    "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve",
    "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "who",
    "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've",
    "your", "yours", "yourself", "yourselves"
]

# Task 3: Analyze text and remove certain words and characters
text = re.sub('[^A-Za-z0-9]+', ' ', text).lower()  # Remove special characters and convert text to lowercase
words = text.split()
filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)

# Task 4: Use Matplotlib to plot a histogram based on the words and counts
word_counts = Counter(filtered_words)
word_counts = word_counts.most_common(10)  # Change the number of top words to plot as needed
words, counts = zip(*word_counts)
plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Counts')
plt.title('Top Words in the Text (excluding stop words)')
plt.show()
