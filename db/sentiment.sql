CREATE TABLE "public"."sentiment_news"
(
    "news_id" bigint NOT NULL,
    "polarity" real NOT NULL,
    "subjectivity" real NOT NULL,
    CONSTRAINT "sentiment_news_news_id" PRIMARY KEY ("news_id"),
    CONSTRAINT "sentiment_news_newsId_fkey" FOREIGN KEY ("news_id") REFERENCES raw_news("id") ON UPDATE CASCADE ON DELETE NO ACTION
    NOT DEFERRABLE
)
WITH (oids = false);