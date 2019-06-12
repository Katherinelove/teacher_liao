# -*- coding: utf-8 -*-

"""
flask 用法
在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。
Flask通过request.form['name']来获取表单的内容
"""


__author__ = 'katherinelove'

from flask import Flask,request

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    return "<h1>Home</h1>"

@app.route("/signin",methods=["GET"])
def signin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route("/signin",methods=["POST"])
def sginin():
    # 需要从request对象读取表单内容：
    userName=request.form["username"]
    password=request.form["password"]
    if userName=="love" and password=="123456":
        return  '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
    app.run()