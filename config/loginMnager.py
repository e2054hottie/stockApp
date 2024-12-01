from dao.userDao import UserDao
from flask_login import LoginManager
from controller.__init__ import app
#インスタンス化
login_manager = LoginManager()
#アプリをログイン機能を紐付ける
login_manager.init_app(app)
#未ログインユーザーを転送する(ここでは'login'ビュー関数を指定)
login_manager.login_view = 'login'

#現在のログインユーザーの情報を保持し、必要なときに参照できるようになる。
@login_manager.user_loader
def load_user(id):
    userDao = UserDao()
    return userDao.user_select(id)
