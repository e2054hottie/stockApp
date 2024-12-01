from dao.userDao import UserDao
from werkzeug.security import generate_password_hash, check_password_hash

class SignupService:
    def __init__(self):
        self.userDao = UserDao()

    def registUser(self,form):
        # ユーザー名
        userName = form["username"]
        # メアド
        email = form["email"]
        # パスワード
        password = form["password"]
        password = generate_password_hash(password)
        self.userDao.user_insert(userName,email,password)