from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_regist(object):
    def setupUi(self, User_regist):
        User_regist.setObjectName("User_regist")
        User_regist.resize(408, 211)
        self.register_2 = QtWidgets.QLabel(User_regist)
        self.register_2.setGeometry(QtCore.QRect(10, 10, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.register_2.setFont(font)
        self.register_2.setAlignment(QtCore.Qt.AlignCenter)
        self.register_2.setObjectName("register_2")

        self.retranslateUi(User_regist)
        QtCore.QMetaObject.connectSlotsByName(User_regist)

    def retranslateUi(self, User_regist):
        _translate = QtCore.QCoreApplication.translate
        User_regist.setWindowTitle(_translate("User_regist", "Form"))
        self.register_2.setText(_translate("User_regist", "You are registered in the system"))
