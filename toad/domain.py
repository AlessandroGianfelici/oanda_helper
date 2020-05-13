# classi per i dati di dominio
from toad.constants import unknown_token


class NewsSentiment:
    def __init__(self, newsId, polarity, subjectivity):
        self._newsId = newsId
        self._polarity = polarity
        self._subjectivity = subjectivity

    def __str__(self):
        return f"NewsSentiment({self.newsId}, {self.polarity})"

    @property
    def newsId(self): return self._newsId

    @property
    def polarity(self): return self._polarity

    @property
    def subjectivity(self): return self._subjectivity

# tag==topic


class RawNews:
    def __init__(self, source, author, title, content, publishedAt, tag):
        self._source = source
        self._author = author if author else unknown_token
        self._title = title if title else unknown_token
        self._content = content
        self._publishedAt = publishedAt
        self._tag = tag

    def __str__(self):
        return f"RawNews({self.source}, {self.author}, {self.title})"

    @property
    def source(self): return self._source

    @property
    def author(self): return self._author

    @property
    def title(self): return self._title

    @property
    def content(self): return self._content

    @property
    def publishedAt(self): return self._publishedAt

    @property
    def tag(self): return self._tag


class RawNewsWithId(RawNews):
    def __init__(self, rawNews, id):
        RawNews.__init__(self, rawNews.source, rawNews.author, rawNews.title,
                         rawNews.content, rawNews.publishedAt, rawNews.tag)
        self._id = id

    @property
    def id(self): return self._id


class Measurement:
    def __init__(self, name, provider, measuredAt, closeAsk, closeBid, highAsk, highBid, lowAsk, lowBid, openAsk, openBid, volume):
        self._name = name
        self._provider = provider
        self._measuredAt = measuredAt
        self._closeAsk = closeAsk
        self._closeBid = closeBid
        self._highAsk = highAsk
        self._highBid = highBid
        self._lowAsk = lowAsk
        self._lowBid = lowBid
        self._openAsk = openAsk
        self._openBid = openBid
        self._volume = volume

    def __str__(self):
        return f"Measurement({self.name}, {self.volume}, {self.measuredAt}, ask: [{self.lowAsk, self.highAsk}], bid: [{self.lowBid, self.highBid}])"

    @property
    def name(self): return self._name

    @property
    def provider(self): return self._provider

    @property
    def measuredAt(self): return self._measuredAt

    @property
    def closeAsk(self): return self._closeAsk

    @property
    def closeBid(self): return self._closeBid

    @property
    def highAsk(self): return self._highAsk

    @property
    def highBid(self): return self._highBid

    @property
    def lowAsk(self): return self._lowAsk

    @property
    def lowBid(self): return self._lowBid

    @property
    def openAsk(self): return self._openAsk

    @property
    def openBid(self): return self._openBid

    @property
    def volume(self): return self._volume
