from dao.userDao import UserDao
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from config.loginMnager import login_manager

@login_manager.user_loader
def load_user(id):
    userDao = UserDao()
    return userDao.user_select(int(id))

class User(UserMixin):
    def __init__(self):
        self.id = None
        self.username= None
        self.email= None
        self.created_at= None
        self.password = None
    def __str__(self):
        return f"[id={self.id},username={self.username},self.email={self.email},created_at={self.created_at}]"

    def check_password(self, password):
        return check_password_hash(self.password,password)