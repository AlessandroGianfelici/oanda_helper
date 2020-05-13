CREATE SEQUENCE "instruments_measurement_Id_seq"
START 1;

CREATE TABLE "public"."instruments_measurement"
(
    "id" bigint DEFAULT nextval('"instruments_measurement_Id_seq"') NOT NULL,
    "name" character(20) NOT NULL,
    "provider" character(50) NOT NULL,
    "measured_at" timestamp NOT NULL,
    "close_ask" real NOT NULL,
    "close_bid" real NOT NULL,
    "high_ask" real NOT NULL,
    "high_bid" real NOT NULL,
    "low_ask" real NOT NULL,
    "low_bid" real NOT NULL,
    "open_ask" real NOT NULL,
    "open_bid" real NOT NULL,
    "volume" integer NOT NULL,
    CONSTRAINT "instruments_measurement_id" PRIMARY KEY ("id")
)
WITH (oids = false);