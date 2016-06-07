import UserDBManager.py

from Project import User


class UserManager:

    userDBManger = UserDBManager()
    user = User()

    def searchUserByEmail(self,email):
        self.userDBManger.searchUser()

    def makeUser(self,email,password,age,gender):
        self.userDBManger.insertUser()

    def modifyUser(self,email,password):
        self.userDBManger.modifyUser()

    def deleteUser(self,email,password):
        self.userDBManger.deleteUser()

    def getUserPreferences(self,user):
        self.user = self.userDBManger.searchUser()
        return self.user.getFoodPreference()

    @property
    def getUserDBManger(self):
        return self.userDBManger

    @property
    def getUser(self):
        return self.user

    @userDBManger.setter
    def setUserDBManger(self,userDBManger):
        self.userDBManger = userDBManger

    @user.setter
    def setUser(self,user):
        self.user = user