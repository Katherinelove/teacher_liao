# -*- coding: utf-8 -*-

"""温习"""

__author__ = 'katherinelove'

import sqlite3

if __name__ == '__main__':
    con=sqlite3.connect("D:\sqldb\love.db")
    cur=con.cursor()
    cur.execute(r"drop table if exists person")
    cur.execute(r"create table person (id integer primary key,name varchar(20),age integer)")
    sql="insert into person (id,name,age) values (%d,%s,%d)"
    cur.execute(sql%(1,"lj",20))
    cur.execute(sql%(1,"kate",25))
    cur.execute(sql%(1,"love",18))
    con.commit()
    cur.execute(r"select * from person")
    results=cur.fetchall()
    print("id\tname\tage")
    for line in results:
        for item in line:
            print(str(item)+"\t",end="")
        print()
    con.close()