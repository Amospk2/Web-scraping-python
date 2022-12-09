import snscrape.modules.twitter as snstwitter
import pandas as pd
import re

tweets_for_gaules = []


def clean_text(tweet_text):
    clean_text = re.sub(r"RT+", "", tweet_text)
    clean_text = re.sub(r"@\s", "", clean_text)
    clean_text = clean_text.replace("\n", " ")
    return clean_text


for count, tweets in enumerate(snstwitter.TwitterUserScraper('Gaules').get_items()):
    if count < 10:
        tweets_for_gaules.append([clean_text(tweets.content), tweets.date, tweets.likeCount])
    else:
        break

df = pd.DataFrame(tweets_for_gaules, columns=['conteudo', 'data', 'likeCount'])
df.to_csv('scrapyGau.csv')

