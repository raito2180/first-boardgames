import json
import random
from flask import Flask,render_template,make_response

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html',person=name)

@app.route('/')
def index():
    return render_template('top.html')

@app.route('/match/')
def match():
    match_games = "data/match.json"
    with open(match_games, 'r') as file:
        match_games_data = json.load(file)
    match_games_list = match_games_data["games"]
    match_game_data = random.choice(match_games_list)
    return render_template('game.html', game=match_game_data)

@app.route('/middle/')
def middle():
    middle_games = "data/middle.json"
    with open(middle_games, 'r') as file:
        middle_games_data = json.load(file)
    middle_games_list = middle_games_data["games"]
    middle_game_data = random.choice(middle_games_list)
    return render_template('game.html', game=middle_game_data)

@app.route('/many/')
def many():
    many_games = "data/many.json"
    with open(many_games, 'r') as file:
        many_games_data = json.load(file)
    many_games_list = many_games_data["games"]
    many_game_data = random.choice(many_games_list)
    return render_template('game.html', game=many_game_data)

@app.errorhandler(404)
def not_found(error):
    # render_template() で生成したレスポンスボディを、make_response() で
    # レスポンスオブジェクトに変換する
    resp = make_response(render_template('error.html'), 404)
    
    # レスポンスオブジェクトのヘッダーを追加で設定することもできる
    resp.headers['X-Something'] = 'A value'
    
    return resp
