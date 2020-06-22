#!/usr/bin/env python
# -*- coding : UTF-8 -*-

import pymysql as pysql
from random import randint
from random import choice

def main():
    n = 1000

    db = pysql.connect("192.168.31.241", "root", "123456", "BIGDATA")

    cursor = db.cursor()

    for i in range(n):

        # Name: 3-8, Abc
	# 1 lst : ABC, abc
	# 2 ascii : int -> C
	## 2 random, chr
        l = randint(3,8) 
	name = ""
	name += chr(randint(65, 90))
	for _ in range(l - 1):
	    name += chr(randint(97, 122))
       
        # Age: 18-55
	age = randint(18,55)

        # Gender : "M", "F"
	genders = ['M', 'F']	
	gender = choice(genders)

        # Income: 1000-10000
	income = randint(1000,10000)

        sql = "INSERT INTO EMPLOYEE (NAME, AGE, GENDER, INCOME) VALUES ('%s', '%s', '%s', '%s')" % (name, age, gender, income)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            #print(e)
            db.rollback()

    db.close()

if __name__ == "__main__":
    main()
