# -*- encoding=utf-8 -*-

from web.pyscript.Model.Singleton import Singleton
from web.pyscript.Model.User import User
from web.pyscript.Controller.UserDBManager import UserDBManger

#유저 객체를 관리하는 매니저 클래스

class UserManager(metaclass=Singleton):

    def __init__(self):
        self._userDBManager = UserDBManger()
