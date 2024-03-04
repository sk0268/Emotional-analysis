import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample dark web forum post (replace with actual data)
dark_web_post = input("Enter your message: ")

# Perform sentiment analysis
sentiment_score = sia.polarity_scores(dark_web_post)

# Interpret sentiment score
if sentiment_score['compound'] <= -0.05:
    print("Potential threat detected: Negative sentiment")
elif sentiment_score['compound'] >= 0.05:
    print("No immediate threat detected: Positive sentiment")
else:
    print("Neutral sentiment: Further analysis may be needed")
