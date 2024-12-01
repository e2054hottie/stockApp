import random
import dao.userDao
import datetime


def ini():
    userDao = dao.userDao.UserDao()
    return list(map(lambda x:x.__str__(), userDao.user_select_all()))
