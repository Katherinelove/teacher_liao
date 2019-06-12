# -*- coding: utf-8 -*-

"""
Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。
Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，这样，我们就成功地把Python代码和HTML代码最大限度地分离了。
使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。
在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。

除了Jinja2，常见的模板还有：
Mako：用<% ... %>和${xxx}的一个模板；
Cheetah：也是用<% ... %>和${xxx}的一个模板；
Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
"""

__author__ = 'katherinelove'



from flask import Flask,request,render_template

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)
#Flask通过render_template()函数来实现模板的渲染。
#最后，一定要把模板放到正确的templates目录下，templates和MVC_模板.py在同级目录下：
if __name__ == '__main__':
    app.run()