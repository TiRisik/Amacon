from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_No_User(object):
    def setupUi(self, No_User):
        No_User.setObjectName("No_User")
        No_User.resize(408, 211)
        self.no_user = QtWidgets.QLabel(No_User)
        self.no_user.setGeometry(QtCore.QRect(10, 10, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.no_user.setFont(font)
        self.no_user.setAlignment(QtCore.Qt.AlignCenter)
        self.no_user.setObjectName("no_user")

        self.retranslateUi(No_User)
        QtCore.QMetaObject.connectSlotsByName(No_User)

    def retranslateUi(self, No_User):
        _translate = QtCore.QCoreApplication.translate
        No_User.setWindowTitle(_translate("No_User", "Form"))
        self.no_user.setText(_translate("No_User", "There is no user with this nickname"))
