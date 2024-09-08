import json
import random
from flask import Flask,render_template,make_response, url_for

app = Flask(__name__)

@app.route('/')
def index():
    ogp_data = {
        'title': 'TOP',
        'description': 'ボドゲを始めるのに間違いないゲームをご紹介しています♪',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('index', _external=True)
    }
    return render_template('top.html', ogp_data=ogp_data)

@app.route('/match/')
def match():
    ogp_data = {
        'title': '対戦用ボドゲ',
        'description': '対戦用ボドゲのおすすめページです。',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('match', _external=True)
    }
    match_games = "data/match.json"
    with open(match_games, 'r') as file:
        match_games_data = json.load(file)
    match_games_list = match_games_data["games"]
    match_game_data = random.choice(match_games_list)
    return render_template('game.html', game=match_game_data, ogp_data=ogp_data)

@app.route('/middle>')
def middle():
    ogp_data = {
        'title': '2~4人用ボドゲ',
        'description': '2~4人用ボドゲのおすすめページです。',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('middle', _external=True)
    }
    middle_games = "data/middle.json"
    with open(middle_games, 'r') as file:
        middle_games_data = json.load(file)
    middle_games_list = middle_games_data["games"]
    middle_game_data = random.choice(middle_games_list)
    return render_template('game.html', game=middle_game_data, ogp_data=ogp_data)

@app.route('/many/')
def many():
    ogp_data = {
        'title': '大人数用ボドゲ',
        'description': '大人数用ボドゲのおすすめページです。',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('many', _external=True)
    }
    many_games = "data/many.json"
    with open(many_games, 'r') as file:
        many_games_data = json.load(file)
    many_games_list = many_games_data["games"]
    many_game_data = random.choice(many_games_list)
    return render_template('game.html', game=many_game_data, ogp_data=ogp_data)

@app.route('/vision/')
def vision():
    ogp_data = {
        'title': '作者紹介',
        'description': '作者を紹介しています。安心してアプリを使用する参考にしてください♪',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('vision', _external=True)
    }
    profile_path = "data/profile.json"
    with open(profile_path, 'r') as file:
        profile_data = json.load(file)
    profile = profile_data["profile"]
    return render_template('vision.html', profile=profile, ogp_data=ogp_data)

@app.route('/qr/')
def qr():
    ogp_data = {
        'title': 'QRコード',
        'description': 'サイトのQRコードです。共有の際にご使用ください！',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('qr', _external=True)
    }
    return render_template('qr.html', ogp_data=ogp_data)

@app.route('/contact/')
def contact():
    ogp_data = {
        'title': 'お問い合わせ',
        'description': '何かあればお気軽にお問い合わせください♪',
        'image': url_for('static', filename='images/ogp.png', _external=True),
        'url': url_for('contact', _external=True)
    }
    return render_template('contact.html', ogp_data=ogp_data)

@app.errorhandler(404)
def not_found(error):
    # render_template() で生成したレスポンスボディを、make_response() で
    # レスポンスオブジェクトに変換する
    resp = make_response(render_template('error.html'), 404)
    
    # レスポンスオブジェクトのヘッダーを追加で設定することもできる
    resp.headers['X-Something'] = 'A value'
    
    return resp
