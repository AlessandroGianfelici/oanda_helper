# toad

A bot that tries to find relationships between news and stock values

## how to run

1. Install Python3 - Pip3
2. Execute prerequisites.sh script to install python dependencies
3. Run one of the python file running

```
pytget_top_headlinesget_top_headlinesget_top_headlineshon3 [file name]

python3 oanda_test.py to perform plot test
python3 importer.py to start real data import (wip)
```

# create database

first of all, install docker on your system: https://docs.docker.com/install/

then, with a terminal on the project root folder, execute:
```
sudo docker-compose up -d
```

first time you do this operation, docker will automatically pull necessary images and run it.

then you can see them running with the command:
```
sudo docker-ps
```
## using adminer ui

at this point, point a browser to address: `localhost:8081`
and login with `Server: db, User: asd, Password: asd, Database: toad`

then, to create toad database just use adminer to import the *.sql files that you can find in db folder

## by command line

to install command line client, see https://help.ubuntu.com/community/PostgreSQL 
(if you're not using ubuntu, you're on your own ¯\_(ツ)_/¯ )

start with a terminal in db folder, then execute the following (using "asd" asd password, when requested):

```
psql -h 0.0.0.0 toad asd -f measurement.sql
psql -h 0.0.0.0 toad asd -f news.sql
psql -h 0.0.0.0 toad asd -f tweets.sql
psql -h 0.0.0.0 toad asd -f sentiment.sql
```

## big database operations

backup

```
psql -h 0.0.0.0 toad asd -c "\copy [TABLE_NAME] to 'backup.csv' csv"
```

restore

```
psql -h 0.0.0.0 toad asd -c "\copy [TABLENAME] FROM 'backup.csv' DELIMITER ',' csv"
```

## clean database

destroy:
```
psql -h 0.0.0.0 postgres asd -c "DROP DATABASE toad;"
```

recreate:
```
psql -h 0.0.0.0 postgres asd -c "CREATE DATABASE toad;"
```

now you need to create tables again, see first two paragraph of this section