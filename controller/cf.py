#coding:utf-8

from flask import Flask, render_template, request
from flask_login import login_required
from service import ap,fincanceData
from . import app

class CashFlowController:
    @app.route('/cf')
    @login_required
    def cf():
        return render_template('cf.html')

    