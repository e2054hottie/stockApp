from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from dao.userDao import UserDao
from service import ap,fincanceData,init_db
from service.loginService import LoginService
from . import app

class LoginController:
    loginService = LoginService()
    @app.route("/login",methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            form = request.form
            user = LoginController.loginService.login(form)
            if user is not None :
                login_user(user)
                return redirect("/top")
        else:
            return render_template('login.html')