CREATE SEQUENCE "raw_news_Id_seq"
START 1;

CREATE TABLE "public"."raw_news"
(
    "id" bigint DEFAULT nextval('"raw_news_Id_seq"') NOT NULL,
    "source" text NOT NULL,
    "author" text NOT NULL,
    "title" text NOT NULL,
    "content" text NOT NULL,
    "published_at" timestamp NOT NULL,
    "tag" text NOT NULL,
    CONSTRAINT "raw_news_id" PRIMARY KEY ("id")
)
WITH (oids = false);