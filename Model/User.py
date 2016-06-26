#-*- encoding=utf-8 -*-


class User:

    def __init__(self, ID, email, password, age):
        '''
        사용자 정보를 가지고 있는 클래스
        :param ID: 사용자 ID (integer)
        :param email: 사용자 email (string)
        :param password: 사용자 password (string)
        :param age: 사용자 나이 (integer)
        '''
        self.ID = ID
        self.email = email
        self.password = password
        self.age = age

    def __repr__(self):
        return "User(ID = %d, email = %s, password = %s, age = %d)"%(self._ID, self._email, self._password, self._age)


    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @ID.deleter
    def ID(self):
        del self._ID

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @password.deleter
    def password(self):
        del self._password

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age