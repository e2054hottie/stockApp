import random
import dao.userDao
import datetime

from entity import User


def ini():
    userDao = dao.userDao.UserDao()
    user = User.User()
    user.id = 1
    print(userDao.user_select(1))
    return list(map(lambda x:x.__str__(), userDao.sel(user)))
