from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wrong_password(object):
    def setupUi(self, Wrong_password):
        Wrong_password.setObjectName("Wrong_password")
        Wrong_password.resize(408, 211)
        self.register_2 = QtWidgets.QLabel(Wrong_password)
        self.register_2.setGeometry(QtCore.QRect(10, 10, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.register_2.setFont(font)
        self.register_2.setAlignment(QtCore.Qt.AlignCenter)
        self.register_2.setObjectName("register_2")

        self.retranslateUi(Wrong_password)
        QtCore.QMetaObject.connectSlotsByName(Wrong_password)

    def retranslateUi(self, Wrong_password):
        _translate = QtCore.QCoreApplication.translate
        Wrong_password.setWindowTitle(_translate("Wrong_password", "Form"))
        self.register_2.setText(_translate("Wrong_password", "You entered an incorrect password"))
