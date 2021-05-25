# -*- coding: utf-8 -*-
# 기본 템플릿

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from flask import Flask
from flask import redirect

from blueprint.predict_blueprint import candidate_blue

# 서버역할을 할 객체 생성
app = Flask(__name__, static_folder='static')
app.register_blueprint(candidate_blue)


# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/')
def home():    
    
    df = pd.read_csv('static/data/keysentences2030.csv')
    return render_template('index.html', df=df)
    
# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/test')
def test():    
    
    return render_template('test.html')

# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/test2')
def test2():    
    
    return render_template('subpages/test_linechart.html')

@app.route('/test3')
def test3():    
    
    return render_template('subpages/test_wordcloud.html')
           
                                        

if __name__ == '__main__':
    app.run(debug=True)
# app.run(host="0.0.0.0", port="8080")