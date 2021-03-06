from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_character(object):
    def setupUi(self, character):
        character.setObjectName("character")
        character.resize(897, 678)
        self.image = QtWidgets.QLabel(character)
        self.image.setGeometry(QtCore.QRect(20, 30, 361, 321))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayoutWidget = QtWidgets.QWidget(character)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(390, 20, 491, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fio = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fio.setFont(font)
        self.fio.setObjectName("fio")
        self.verticalLayout.addWidget(self.fio)
        self.age = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.verticalLayout.addWidget(self.age)
        self.race = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.race.setFont(font)
        self.race.setObjectName("race")
        self.verticalLayout.addWidget(self.race)
        self.gender = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.verticalLayout.addWidget(self.gender)
        self.weight = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.verticalLayout.addWidget(self.weight)
        self.height = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.verticalLayout.addWidget(self.height)
        self.biography = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.biography.setObjectName("biography")
        self.verticalLayout.addWidget(self.biography)
        self.appearance = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.appearance.setObjectName("appearance")
        self.verticalLayout.addWidget(self.appearance)
        self.character1 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.character1.setObjectName("character1")
        self.verticalLayout.addWidget(self.character1)

        self.retranslateUi(character)
        QtCore.QMetaObject.connectSlotsByName(character)

    def retranslateUi(self, character):
        _translate = QtCore.QCoreApplication.translate
        character.setWindowTitle(_translate("character", "Form"))
        self.image.setText(_translate("character", "Image"))
        self.fio.setText(_translate("character", "Name and surname"))
        self.age.setText(_translate("character", "Age"))
        self.race.setText(_translate("character", "Race"))
        self.gender.setText(_translate("character", "Gender"))
        self.weight.setText(_translate("character", "Weight"))
        self.height.setText(_translate("character", "Height"))