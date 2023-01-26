from flask import url_for
from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/')
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
