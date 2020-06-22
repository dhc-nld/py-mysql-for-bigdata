#!/usr/bin/env python
# -*- coding : UTF-8 -*-

import pymysql as pysql

def main():
    db = pysql.connect("192.168.31.241", "root", "123456", "BIGDATA")

    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    sql = """CREATE TABLE EMPLOYEE (
             NAME CHAR(20) NOT NULL,
             AGE INT,
             GENDER CHAR(1),
             INCOME FLOAT)"""

    cursor.execute(sql)

    db.close()

if __name__ == "__main__":
    main()
