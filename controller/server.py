#coding:utf-8

from flask import Flask, render_template, request
from  main import app
from service import ap
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    req1 = request.form['data1']
    return render_template('result.html',insert_something =ap.test(req1))