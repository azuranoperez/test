
import MySQLdb

#Problem - Part 2

#The second part of the challenge is a programming test. This test should be completed in python and the resulting scripts should be checking into a public GIT repository with the link provided to us before the interview. (no access credentials are to be put into the GIT repo).

############ First task file loading #############

#The task is to download the three files from Cloud Storage and upload them into three new tables that you will create within a MySQL Cloud Database, This will include any relationships you feel would be appropriate between the sets of data. 

# This script creates a DB im and upload the three files

host = 'localhost'
user = 'root'
passwd = ''

connection = MySQLdb.connect(host, user, passwd)
cursor = connection.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS im""")

connection.commit()

cursor.execute("""USE im""")

cursor.execute("""CREATE TABLE countries (
id smallint(4) unsigned NOT NULL,
alpha2 char(2),
alpha3 char(3),
name varchar(50),
targetable tinyint(1),
PRIMARY KEY (id)) """
)

cursor.execute("""CREATE TABLE regions (
id smallint(4) unsigned NOT NULL,
country_id smallint(4) unsigned NOT NULL,
name varchar(40) NOT NULL,
iso_code char(3),
PRIMARY KEY (id),
INDEX coun_id (country_id),
FOREIGN KEY (country_id) REFERENCES countries(id))"""
)

cursor.execute("""CREATE TABLE cities (
id mediumint(6) unsigned NOT NULL,
country_id smallint(4) unsigned NOT NULL,
region_id smallint(4) unsigned NOT NULL,
name varchar(40) NOT NULL,
iso_code char(4),
PRIMARY KEY (id))"""
)

# Loading the files:

# cities file needs to be converted from json to csv using the script below:

convertocsv.py

cursor.execute("""LOAD DATA LOCAL INFILE '/home/valgar/infectious/countries.csv' INTO TABLE countries FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS""")

cursor.execute("""LOAD DATA LOCAL INFILE '/home/valgar/infectious/cities.csv' INTO TABLE cities FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' """)

cursor.execute("""LOAD DATA LOCAL INFILE '/home/valgar/infectious/regions.csv' INTO TABLE regions FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS""")

# Once completed you should also create a user within the DB who has view access to the three new tables.

# Create the username and assign the privilegies:

cursor.execute("""CREATE USER 'imuser'@'localhost' IDENTIFIED BY 'password'""");

cursor.execute("""GRANT SELECT ON im.* TO 'imuser'@'localhost'""");

