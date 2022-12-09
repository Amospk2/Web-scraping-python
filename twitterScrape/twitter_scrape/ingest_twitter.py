import snscrape.modules.twitter as snstwitter
import pandas as pd
import re
import argparse
from sqlalchemy import create_engine


def main(params):
    hashtag = params.query
    posts = []

    engine = create_engine("mysql://Amospk2:root@127.0.0.1/twitterScrape")
    engine.connect()

    def clean_text(tweet_text):
        clean_text = re.sub(r"RT+", "", tweet_text)
        clean_text = re.sub(r"@\s", "", clean_text)
        clean_text = clean_text.replace("\n", " ")
        return clean_text

    for count, tweet in enumerate(snstwitter.TwitterSearchScraper(hashtag).get_items()):
        if count > 100:
            break
        else:
            tweet.rawContent = clean_text(tweet.content)
            posts.append([tweet.id, tweet.user.username, tweet.date, tweet.content])

    df = pd.DataFrame(posts, columns=(["id", "username", "date", "conteudo"]))
    df.to_sql(params.table_name, con=engine, if_exists='append')


if __name__ == '__main__':
    twitter_scrappe_parser = argparse.ArgumentParser(description="Scrape para o twitter")
    twitter_scrappe_parser.add_argument('--query',type=str, help="query para o scrape") 
    twitter_scrappe_parser.add_argument('--table_name',type=str, help="name do arquivo resultante") 
    twitter_scrappe_parser = twitter_scrappe_parser.parse_args()
    main(twitter_scrappe_parser)







