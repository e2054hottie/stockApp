#coding:utf-8

from flask import Flask, render_template, request
from flask_login import current_user,login_required
from service import ap,fincanceData
from service.cfService import CfService
from . import app

class CashFlowController:
    cfService = CfService()
    @app.route('/cf')
    @login_required
    def cf():
        expenses = CashFlowController.cfService.get_expenses(int(current_user.get_id()))
        return render_template('cash_flow.html',expenses=expenses)
    
    @app.route('/cf/regist_expenditure',methods=["POST"])
    @login_required
    def cf_regist_expenditure():
        form = request.form
        CashFlowController.cfService.regist_expense(form,int(current_user.get_id()))
        expenses = CashFlowController.cfService.get_expenses(int(current_user.get_id()))
        return render_template('cash_flow.html',expenses=expenses)

    