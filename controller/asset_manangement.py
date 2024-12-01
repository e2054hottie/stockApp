#coding:utf-8

from flask import Flask, render_template, request
from service import ap,fincanceData
from service.assetManagementService import AssetManagementService
from . import app
from flask_login import current_user,login_required

class AssetManagementController:
    assetManagementService = AssetManagementService()

    @app.route('/am',methods=["GET", "POST"])
    @login_required
    def am():
        stockData = AssetManagementController.assetManagementService.getStockData(int(current_user.get_id()))
        if request.method == "POST":
            form = request.form
            print(form)
            AssetManagementController.assetManagementService.regist(form,int(current_user.get_id()))
            return render_template('asset_management.html',stocks=stockData)
        else :
            return render_template('asset_management.html',stocks=stockData)