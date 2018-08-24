import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
for tweet in tweetData:
    tweetBlob = TextBlob("Tweet text: " + tweet["text"])
    polarity.append(tweetBlob.polarity)

print(polarity)
print(subjectivity)


plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 6])
plt.grid(True)
plt.show()

sub.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
sub.xlabel('Values')
sub.ylabel('Number of Items')
sub.title('Histogram of Numbers')
sub.axis([-1.1, 1.1, 0, 6])
sub.grid(True)
sub.show()
