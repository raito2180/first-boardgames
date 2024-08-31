from flask import Flask,render_template,make_response

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html',person=name)

@app.route('/')
def index():
    return render_template('top.html')

@app.route('/right/')
def right():
    return render_template('right.html')

@app.route('/heavy/')
def heavy():
    return render_template('heavy.html')

@app.errorhandler(404)
def not_found(error):
    # render_template() で生成したレスポンスボディを、make_response() で
    # レスポンスオブジェクトに変換する
    resp = make_response(render_template('error.html'), 404)
    
    # レスポンスオブジェクトのヘッダーを追加で設定することもできる
    resp.headers['X-Something'] = 'A value'
    
    return resp
