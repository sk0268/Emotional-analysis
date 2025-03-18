import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
dark_web_post = input("Enter your message: ")
sentiment_score = sia.polarity_scores(dark_web_post)
if sentiment_score['compound'] <= -0.05:
    print("Potential threat detected: Negative sentiment")
elif sentiment_score['compound'] >= 0.05:
    print("No immediate threat detected: Positive sentiment")
else:
    print("Neutral sentiment: Further analysis ma be needed")
