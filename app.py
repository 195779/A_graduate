from flask import url_for
from markupsafe import escape
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #导入数据库映射类
from flask import render_template
import os
import sys
import click

app = Flask(__name__)

# 第二章：HelloFlask

@app.route('/index')
@app.route('/home')
def hello():
    return '欢迎来到我的 A_graduate!'

@app.route('/firstPicture')
def showPicture():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test/')
def test_url_for():
    print(url_for('hello'))  
    #生成hello视图函数对应的URL
    #将会在命令行输出：/home
    #命令行输出：/user/cym_alan_test1
    print(url_for('user_page', name='cym_alan_test1'))
    #user_page 函数需要一个name类型的变量，赋值一个name
    print(url_for('user_page', name='alantam'))  #命令行输出：/user/alantam
    print(url_for('test_url_for'))  # 命令行输出：/test
    print(url_for('test_url_for', num=2))  # 命令行输出：/test?num=2
    return 'Test page'

@app.route('/User/<int:number>')  #将number转换为整型
def test_number(number):
    print('number:',number)#命令行打印
    return f'User:{escape(number)}'
    #界面打印
    #用户输入的数据会包含恶意代码，所以不能直接作为响应返回，
    #需要使用 MarkupSafe（Flask 的依赖之一）提供的 escape() 函数对 name 变量进行转义处理
    #比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行

    #以 . 开头的文件默认会被隐藏，执行ls命令看不见他们，需要执行ls -f 

# 第三章：模板


@app.cli.command()
def forge():
    db.create_all()
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'}, 
        ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title = m['title'],year = m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)

#第五章：数据库
WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)#初始化扩展，传入程序实例 app

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份

