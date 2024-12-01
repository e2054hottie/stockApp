from dao.userDao import UserDao
from werkzeug.security import generate_password_hash, check_password_hash

class LoginService:
    
    def __init__(self):
        self.userDao = UserDao()

    def login(self,form):
        """概要
        ログインに成功した場合はそのユーザーを，失敗した場合はNoneを返す
        """
        # メアド
        email = form["email"]
        # パスワード
        password = form["password"]
        
        # ユーザーを取得
        user = self.userDao.user_select_by_email(email)
        print("user=",user.username,user.password)
        if user is not None:
            if user.check_password(password):
                return user
        return None