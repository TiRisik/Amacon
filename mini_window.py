from no_user import Ui_No_User
from us_reg import Ui_User_regist
from wrongpass import Ui_Wrong_password
from PyQt5.QtWidgets import QWidget


class NoUser(QWidget, Ui_No_User):
    def __init__(self):
        super(NoUser, self).__init__()
        self.setupUi(self)


class UserRegistered(QWidget, Ui_User_regist):
    def __init__(self):
        super(UserRegistered, self).__init__()
        self.setupUi(self)


class WrongPassword(QWidget, Ui_Wrong_password):
    def __init__(self):
        super(WrongPassword, self).__init__()
        self.setupUi(self)