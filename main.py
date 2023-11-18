from textblob import TextBlob

print("hello, I am a program that can recognize emotions in text,\n write something here and I will tell you how positive or\n negative the emotions are in the text: ")
# Sample text for emotion analysis
text = input()

# Create a TextBlob object
blob = TextBlob(text)

# Get the sentiment and emotion
sentiment = blob.sentiment.polarity
emotion = blob.sentiment

# Determine emotion based on sentiment score
if sentiment > 0:
    print("Positive Emotion")
elif sentiment < 0:
    print("Negative Emotion")
else:
    print("Neutral Emotion")

# Print emotion details
print("Emotion Polarity:", sentiment)
print("Emotion Assessment:", emotion)
