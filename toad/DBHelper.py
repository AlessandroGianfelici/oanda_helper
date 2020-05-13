import psycopg2
import logging
from toad.domain import RawNewsWithId
from functools import reduce

# dummy implementation of dbHelper that does nothing but logging


class DBHelper:
    def __init__(self):
        logging.info("opening db connection")
        self._db = psycopg2.connect(
            "dbname=toad user=asd password=asd host=0.0.0.0 port=5432")

    def findLastTweetIdForAuthor(self, author):
        with self._db.cursor() as cur:
            cur.execute(
                "select max(id) from tweets where author= %s ", [author])
            result = cur.fetchone()[0]
            return 0 if result == None else result

    def tweetToTuple(self, tweet):
        return (tweet.id,
                tweet.full_text,
                tweet.created_at,
                tweet.favorite_count,
                tweet.user.screen_name,
                tweet.user.followers_count,
                tweet.user.location)

    def insertTweets(self, tweets):
        with self._db.cursor() as cur:
            cur.executemany("INSERT INTO tweets (id, text, date, likes, author, followers, location) " +
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)", map(self.tweetToTuple, tweets))
            # qui si potrebbe ottimizzare ulterormente con un unico batchone, flattenizzando tutto
            for tag_tuple in filter(lambda tag_tuple: len(tag_tuple[1]) > 0, map(lambda tweet: (tweet.id, tweet.hashtags), tweets)):
                tags = map(lambda t: (tag_tuple[0], t.text), tag_tuple[1])
                cur.executemany(
                    "INSERT INTO tweets_hashtags (id, tag) VALUES (%s, %s)", tags)
            self._db.commit()

    # insert measurement and returns id
    def insertMeasuement(self, measurement):
        with self._db.cursor() as cur:
            cur.execute("INSERT INTO instruments_measurement (name,provider,measured_at,close_ask,close_bid,high_ask,high_bid,low_ask,low_bid,open_ask,open_bid,volume) " +
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",
                        (measurement.name,
                         measurement.provider,
                         measurement.measuredAt,
                         measurement.closeAsk,
                         measurement.closeBid,
                         measurement.highAsk,
                         measurement.highBid,
                         measurement.lowAsk,
                         measurement.lowBid,
                         measurement.openAsk,
                         measurement.openBid,
                         measurement.volume
                         ))
            id = cur.fetchone()[0]
            self._db.commit()
            return id

    def insertRawNewsAndRetrieveWithIdSingle(self, news):
        with self._db.cursor() as cur:
            cur.execute("INSERT INTO raw_news (source,author,title,content,published_at,tag) " +
                        "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                        (news.source,
                         news.author,
                         news.title,
                         news.content,
                         news.publishedAt,
                         news.tag
                         ))
            id = cur.fetchone()[0]
            self._db.commit()
            return RawNewsWithId(news, id)

    def insertNewsSentimentSingle(self, newsSentiment):
        with self._db.cursor() as cur:
            cur.execute("INSERT INTO sentiment_news (news_id,polarity,subjectivity) " +
                        "VALUES (%s, %s, %s) RETURNING news_id",
                        (newsSentiment._newsId,
                         newsSentiment.polarity,
                         newsSentiment.subjectivity
                         ))
            id = cur.fetchone()[0]
            self._db.commit()
            return id

    # insert raw news list and returns whole objects with their ids
    # TODO: ottimizzare batch insertion
    def insertRawNewsAndRetrieveWithId(self, news):
        return list(map(self.insertRawNewsAndRetrieveWithIdSingle, news))

    def insertNewsSentimentList(self, news):
        return list(map(self.insertNewsSentimentSingle, news))
