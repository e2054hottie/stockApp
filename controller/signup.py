from flask import Flask, render_template, request
from service import ap,fincanceData,init_db
from service.sginupService import SignupService
from . import app

class SignupController:
    signupService = SignupService()
    def __init__():
        pass
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    
    @app.route('/registUser', methods=['POST'])
    def register():
        req1 = request.form
        SignupController.signupService.registUser(req1)
        return render_template('top.html')