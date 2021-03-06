from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(715, 538)
        self.avatar = QtWidgets.QLabel(Setting)
        self.avatar.setGeometry(QtCore.QRect(10, 40, 291, 301))
        self.avatar.setObjectName("avatar")
        self.formLayoutWidget = QtWidgets.QWidget(Setting)
        self.formLayoutWidget.setGeometry(QtCore.QRect(330, 40, 361, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.new_login = QtWidgets.QLabel(self.formLayoutWidget)
        self.new_login.setObjectName("new_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.new_login)
        self.newlogEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newlogEdit.setObjectName("newlogEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.newlogEdit)
        self.passw = QtWidgets.QLabel(self.formLayoutWidget)
        self.passw.setObjectName("passw")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passw)
        self.lastpassedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lastpassedit.setObjectName("lastpassedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastpassedit)
        self.new_pass = QtWidgets.QLabel(self.formLayoutWidget)
        self.new_pass.setObjectName("new_pass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.new_pass)
        self.newpassedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newpassedit.setObjectName("newpassedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.newpassedit)
        self.email = QtWidgets.QLabel(self.formLayoutWidget)
        self.email.setObjectName("email")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.email)
        self.phoneedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneedit.setObjectName("phoneedit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phoneedit)
        self.emailedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailedit.setObjectName("emailedit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.emailedit)
        self.genders = QtWidgets.QLabel(self.formLayoutWidget)
        self.genders.setObjectName("genders")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genders)
        self.gender_user = QtWidgets.QComboBox(self.formLayoutWidget)
        self.gender_user.setObjectName("gender_user")
        self.gender_user.addItem("")
        self.gender_user.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gender_user)
        self.user_age = QtWidgets.QLabel(self.formLayoutWidget)
        self.user_age.setObjectName("user_age")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.user_age)
        self.ageusedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ageusedit.setObjectName("ageusedit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ageusedit)
        self.counrtys = QtWidgets.QLabel(self.formLayoutWidget)
        self.counrtys.setObjectName("counrtys")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.counrtys)
        self.contuseredit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.contuseredit.setObjectName("contuseredit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.contuseredit)
        self.aboutme = QtWidgets.QLabel(self.formLayoutWidget)
        self.aboutme.setObjectName("aboutme")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.aboutme)
        self.textaboutme = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textaboutme.setObjectName("textaboutme")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.textaboutme)
        self.phonenumb = QtWidgets.QLabel(self.formLayoutWidget)
        self.phonenumb.setObjectName("phonenumb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.phonenumb)
        self.saves1 = QtWidgets.QPushButton(Setting)
        self.saves1.setGeometry(QtCore.QRect(570, 460, 111, 51))
        self.saves1.setObjectName("saves1")
        self.picture = QtWidgets.QPushButton(Setting)
        self.picture.setGeometry(QtCore.QRect(10, 370, 131, 23))
        self.picture.setObjectName("picture")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.avatar.setText(_translate("Setting", "Please upload your avatar here"))
        self.new_login.setText(_translate("Setting", "New login"))
        self.passw.setText(_translate("Setting", "Password"))
        self.new_pass.setText(_translate("Setting", "New password"))
        self.email.setText(_translate("Setting", "Email"))
        self.genders.setText(_translate("Setting", "Gender"))
        self.gender_user.setItemText(0, _translate("Setting", "Man"))
        self.gender_user.setItemText(1, _translate("Setting", "Woman"))
        self.user_age.setText(_translate("Setting", "Age"))
        self.counrtys.setText(_translate("Setting", "Country"))
        self.aboutme.setText(_translate("Setting", "About me"))
        self.phonenumb.setText(_translate("Setting", "Phone"))
        self.saves1.setText(_translate("Setting", "Save"))
        self.picture.setText(_translate("Setting", "Choose the picture"))
