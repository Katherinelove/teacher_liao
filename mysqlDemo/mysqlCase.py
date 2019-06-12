# -*- coding: utf-8 -*-

"""mysql applications"""

__author__ = 'katherinelove'

import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host="localhost", user="root",
                         password="123456", db="student",port=3306)
    cur=conn.cursor()
    cur.execute(r"drop table if exists person")
    cur.execute(r"create table person (id int(4) primary key,name varchar(12),age int(4))")
    cur.execute("insert into person values (5,'yuren',25)")
    print(cur.rowcount)
    cur.execute(r"insert into person (id,name,age) values (%s,%s,%s)",(1, "曾帅", 20))
    cur.execute(r"insert into person (id,name,age) values (%s,%s,%s)",(2, "kate", 25))
    cur.execute(r"insert into person (id,name,age) values (%s,%s,%s)",(3, "love", 22))
    conn.commit()
    cur.execute(r"select * from person")
    results = cur.fetchall()
    print("id\tname\tage")
    for line in results:
        for item in line:
            print(str(item) + "\t", end="")
        print()
    conn.close()