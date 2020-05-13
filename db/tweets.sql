CREATE TABLE "public"."tweets"
(
    "id" bigint,
    "text" text NOT NULL,
    "date" timestamp NOT NULL,
    "likes" int NOT NULL,
    "author" text NOT NULL,
    "followers" int NOT NULL,
    "location" text NOT NULL,
    CONSTRAINT "tweet_id" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE TABLE "public"."tweets_hashtags"
(
    "id" bigint,
    "tag" text,
    CONSTRAINT "tweet_id_reference" FOREIGN KEY ("id") REFERENCES tweets("id") ON UPDATE CASCADE ON DELETE CASCADE
) WITH (oids = false);
