#coding:utf8
#Python连接sqlite3
#author:katherinelove
#copyright:shuai


import sqlite3
#con=connect（)返回数据库连接对象
#数据库连接对象有 cursor()  commit()  rollback()   close(）方法
# 没有love.db自动创建数据库
con=sqlite3.connect(r"D:\sqldb\love.db")

#cursor（）方法返回游标对象
cur=con.cursor()
#游标对象有 execute()  executemany() fetchone() fetchmany() fetchall() close() scroll()方法
#建表
#cur.execute(r"create table person (id integer primary key,name varchar(20),age integer)")
#插入数据
####### 一是直插入，容易导致sql注入
#eg data="0,'zengshuai',20"
#cur.execute(r'isnert into person values(%s)'%data)
#######二是采用占位符？，回避这个问题（力推）
#cur.execute('insert into person values (?,?,?)',(0,'zengshuai',25))
#插入多条数据
#cur.executemany('insert into person values(?,?,?)',[(3,'marry',20),(4,'jack',25)])
#插入数据不会立即生效
#con.commit()
#出现错误还可以回滚
#con.rollback()

#查看数据
cur.execute('select * from person')
#取回数据(返回)
result=cur.fetchall()
print("id\tname\tage\t")
for line in result:
    for item in line:
        print(str(item)+"\t",end="")
    print()

#连续选择
cur.execute(r'select * from person where id>?',(2,))
result1=cur.fetchone()
print(result1)

#修改数据
cur.execute('update person set name=? where id=?',('rose',3))
con.commit()
#删除数据
cur.execute('delete from person where id=?',(0,))
con.commit()
#关闭数据库连接对象
con.close()