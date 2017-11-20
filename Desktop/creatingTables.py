#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from dbConnection import config
from mysql.connector import errorcode
import mysql.connector

link = mysql.connector.connect(**config)
cursor = link.cursor(buffered=True)

TABLES = {}

TABLES['films'] = (
    "CREATE TABLE `films` ("
    "  `film_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(100),"
    "  `episode_id` int(5),"
    "  `opening_crawl` varchar(1000),"
    "  `director` varchar(100),"
    "  `producer` varchar(100),"
    "  `release_date` varchar(100),"
    "  `characters` varchar(1000),"
    "  `planets` varchar(1000),"
    "  `starships` varchar(1000),"
    "  `vehicles` varchar(1000),"
    "  `species` varchar(1000),"
    "  `created` varchar(100),"
    "  `edited` varchar(100),"
    "  `url` varchar(100),"
    "  PRIMARY KEY (`film_no`)"
    ") ENGINE=InnoDB")

TABLES['planets'] = (
    "CREATE TABLE `planets` ("
    "  `planet_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(100),"
    "  `rotation_period` int(100),"
    "  `orbital_period` int(100),"
    "  `diameter` int(100),"
    "  `climate` varchar(100),"
    "  `gravity` varchar(100),"
    "  `terrain` varchar(100),"
    "  `surface_water` varchar(100),"
    "  `population` varchar(100),"
    "  `residents` varchar(1000),"
    "  `films` varchar(1000),"
    "  `created` varchar(100),"
    "  `edited` varchar(100),"
    "  `url` varchar(100),"
    "  PRIMARY KEY (`planet_no`)"
    ") ENGINE=InnoDB")

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Data commited and DBlink isclosed
link.commit()

cursor.close()
link.close()