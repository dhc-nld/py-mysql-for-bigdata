#!/usr/bin/env python
# -*- coding : UTF-8 -*-

import pymysql as pysql

db = pysql.connect("192.168.31.241", "root", "123456", "BIGDATA")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version: {}".format(data))

db.close()
