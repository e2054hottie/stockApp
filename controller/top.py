#coding:utf-8

from flask import Flask, render_template, request
from service import ap,fincanceData,init_db
from . import app

class TopController:
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/top')
    def top():
        return render_template("top.html")
    
    @app.route('/analies/stock')
    def analies_stock():
        code = request.args.get('code')
        code = code + ".T"
        return render_template('result.html',insert_something = ap.test2(fincanceData.get_financial_data(code)))

    @app.route('/sampleform-post', methods=['POST'])
    def sample_form_temp():
        req1 = request.form['data1'] + ".T"
        return render_template('result.html',insert_something = ap.test2(fincanceData.get_financial_data(req1)))
    
    @app.route("/init")
    def init():
        result = init_db.ini()
        return render_template("top.html", insert_something= result)