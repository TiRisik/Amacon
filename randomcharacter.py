from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RandomCharacter(object):
    def setupUi(self, RandomCharacter):
        RandomCharacter.setObjectName("RandomCharacter")
        RandomCharacter.resize(897, 678)
        self.image = QtWidgets.QLabel(RandomCharacter)
        self.image.setGeometry(QtCore.QRect(20, 30, 361, 321))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayoutWidget = QtWidgets.QWidget(RandomCharacter)
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
        self.load = QtWidgets.QPushButton(RandomCharacter)
        self.load.setGeometry(QtCore.QRect(50, 582, 121, 31))
        self.load.setObjectName("pushButton")

        self.retranslateUi(RandomCharacter)
        QtCore.QMetaObject.connectSlotsByName(RandomCharacter)

    def retranslateUi(self, RandomCharacter):
        _translate = QtCore.QCoreApplication.translate
        RandomCharacter.setWindowTitle(_translate("RandomCharacter", "Form"))
        self.image.setText(_translate("RandomCharacter", "Image"))
        self.fio.setText(_translate("RandomCharacter", "Name and surname"))
        self.age.setText(_translate("RandomCharacter", "Age"))
        self.race.setText(_translate("RandomCharacter", "Race"))
        self.gender.setText(_translate("RandomCharacter", "Gender"))
        self.weight.setText(_translate("RandomCharacter", "Weight"))
        self.height.setText(_translate("RandomCharacter", "Height"))
        self.load.setText(_translate("RandomCharacter", "Load character"))
