from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.signin = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.signin.setContentsMargins(0, 0, 0, 0)
        self.signin.setObjectName("signin")
        self.logedit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.logedit.setObjectName("logedit")
        self.signin.addWidget(self.logedit, 0, 1, 1, 1)
        self.passedit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passedit.setObjectName("passedit")
        self.signin.addWidget(self.passedit, 1, 1, 1, 1)
        self.password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password.setObjectName("password")
        self.signin.addWidget(self.password, 1, 0, 1, 1)
        self.login = QtWidgets.QLabel(self.gridLayoutWidget)
        self.login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login.setAutoFillBackground(False)
        self.login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login.setObjectName("login")
        self.signin.addWidget(self.login, 0, 0, 1, 1)
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 129, 291, 21))
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(20, 150, 271, 21))
        self.text2.setObjectName("text2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 300, 291, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")
        self.newchar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newchar.setObjectName("newchar")
        self.buttons.addWidget(self.newchar)
        self.mychar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mychar.setObjectName("mychar")
        self.buttons.addWidget(self.mychar)
        self.randomchar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.randomchar.setObjectName("randomchar")
        self.buttons.addWidget(self.randomchar)
        self.search_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_user.setObjectName("Search User")
        self.buttons.addWidget(self.search_user)
        self.setting = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setting.setObjectName("setting")
        self.buttons.addWidget(self.setting)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 180, 321, 92))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.title = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.title.setContentsMargins(0, 0, 0, 0)
        self.title.setObjectName("title")
        self.amacon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Z003 [urw]")
        font.setPointSize(36)
        font.setItalic(True)
        self.amacon.setFont(font)
        self.amacon.setAlignment(QtCore.Qt.AlignCenter)
        self.amacon.setObjectName("amacon")
        self.title.addWidget(self.amacon)
        self.text3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text3.sizePolicy().hasHeightForWidth())
        self.text3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.text3.setFont(font)
        self.text3.setObjectName("text3")
        self.title.addWidget(self.text3)
        self.sign = QtWidgets.QPushButton(self.centralwidget)
        self.sign.setGeometry(QtCore.QRect(120, 100, 80, 23))
        self.sign.setObjectName("pushButton")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(680, 10, 121, 49))
        self.user.setObjectName("user_2")
        self.avatar = QtWidgets.QLabel(self.centralwidget)
        self.avatar.setGeometry(QtCore.QRect(614, 10, 51, 49))
        self.avatar.setObjectName("avatar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.password.setText(_translate("MainWindow", "password"))
        self.login.setText(_translate("MainWindow", "login"))
        self.text1.setText(_translate("MainWindow", "If you are a new user, you will "))
        self.text2.setText(_translate("MainWindow", "be automatically registered"))
        self.newchar.setText(_translate("MainWindow", "New character"))
        self.mychar.setText(_translate("MainWindow", "My characters"))
        self.randomchar.setText(_translate("MainWindow", "Random character"))
        self.search_user.setText(_translate("MainWindow", "Search User"))
        self.setting.setText(_translate("MainWindow", "Setting"))
        self.amacon.setText(_translate("MainWindow", "Amacon"))
        self.text3.setText(_translate("MainWindow", "the constructor of the characters"))
        self.sign.setText(_translate("MainWindow", "Sign in"))
        self.user.setText(_translate("MainWindow", "login of the user"))
        self.avatar.setText(_translate("MainWindow", "avatar"))
