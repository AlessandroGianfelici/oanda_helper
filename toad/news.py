# modulo per recuperare le news

# api: https://newsapi.org/
# API-KEY: 07145c68c0814ae1a55c948a2f0d7ac1
# docs: https://newsapi.org/docs/get-started
from datetime import datetime
from newsapi import NewsApiClient
from toad.domain import RawNews
from toad.constants import newsapi_token
from toad.configReader import ConfigReader
import numpy as np


def retrieveNewsDay(topic, newsapi, day, limit=20):
    day_start = f"{day}T00:00:00"
    day_end = f"{day}T23:59:59"
    return map(lambda x: toDomainNews(x, topic), retrieveNews(topic, newsapi, limit, day_start, day_end))


def retrieveTodayHeadlines(newsapi, limit=30):
    today_news = newsapi.get_top_headlines(language='en', country=[
                                           'us', 'uk'], page_size=limit, category='business')["articles"]
    return map(lambda x: toDomainNews(x, "headline"), today_news)

# should return RawNews, like the other method


def retrieveNews(topic, newsapi, limit=100, from_param=None, to=None):
    today_start = datetime.now().strftime('%Y-%m-%dT00:00:00')
    today_end = datetime.now().strftime('%Y-%m-%dT23:59:59')

    configReader = ConfigReader()
    good_newspapers = ""
    for newspaper in configReader.readNewspaper():
        good_newspapers = good_newspapers + str(newspaper) + ","

    good_newspapers = good_newspapers[:-1]

    from_param = today_start if from_param == None else from_param
    to = today_end if to == None else to

    return newsapi.get_everything(q=topic,
                                  language='en',
                                  from_param=from_param,
                                  to=to,
                                  sort_by="relevancy",
                                  sources=good_newspapers,
                                  page_size=limit)["articles"]


# TODO: implement retrieve news from twitter: https://github.com/bear/python-twitter

def toDomainNews(new, topic):
    return RawNews(new["source"]["id"], new["author"], new["title"], new["content"], new["publishedAt"], topic)


if __name__ == '__main__':
    newsapi = NewsApiClient(api_key=newsapi_token)
    data = retrieveNews('federal reserve', newsapi)
    print(f"I read: {len(data)} articles:")
    list(map(lambda article: print(f'ARTICLE: {article}'), data))

# sources='financial-times'
