import pandas as pd
from flask import Blueprint
from flask import render_template
from flask import session

# blueprint 객체 생성 : 주소 세팅
candidate_blue = Blueprint('candidate', __name__)

@candidate_blue.route('/yoonsy')
def yoonsy():    
    df = pd.read_csv('static/data/윤석열.csv')
    return render_template('subpages/yoonsy.html', df=df)

@candidate_blue.route('/leejm')
def leejm():    
    df = pd.read_csv('static/data/이재명.csv')
    return render_template('subpages/leejm.html', df=df)

@candidate_blue.route('/leeny')
def leeny():    
    df = pd.read_csv('static/data/이낙연.csv')
    return render_template('subpages/leeny.html', df=df)

@candidate_blue.route('/hongjp')
def hongjp():    
    df = pd.read_csv('static/data/홍준표.csv')
    return render_template('subpages/hongjp.html', df=df)

@candidate_blue.route('/anncs')
def anncs():    
    df = pd.read_csv('static/data/안철수.csv')
    return render_template('subpages/anncs.html', df=df)


@candidate_blue.route('/jungsg')
def jungsg():    
    df = pd.read_csv('static/data/정세균.csv')
    return render_template('subpages/jungsg.html', df=df)

@candidate_blue.route('/yusm')
def yusm():    
    df = pd.read_csv('static/data/유승민.csv')
    return render_template('subpages/yusm.html', df=df)

@candidate_blue.route('/simsj')
def simsj():    
    df = pd.read_csv('static/data/심상정.csv')
    return render_template('subpages/simsj.html', df=df)

@candidate_blue.route('/chum')
def chum():    
    df = pd.read_csv('static/data/추미애.csv')
    return render_template('subpages/chum.html', df=df)

@candidate_blue.route('/hwanggy')
def hwanggy():    
    df = pd.read_csv('static/data/황교안.csv')
    return render_template('subpages/hwanggy.html', df=df)

@candidate_blue.route('/kimbg')
def kimbg():    
    df = pd.read_csv('static/data/김부겸.csv')
    return render_template('subpages/kimbg.html', df=df)


