from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyCharacters(object):
    def setupUi(self, MyCharacters):
        MyCharacters.setObjectName("MyCharacters")
        MyCharacters.resize(503, 603)
        self.verticalLayoutWidget = QtWidgets.QWidget(MyCharacters)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 411, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Characters = []
        for i in range(10):
            characterButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
            characterButton.setObjectName(f"Character_{i + 1}")
            self.verticalLayout.addWidget(characterButton)
            self.Characters.append(characterButton)

        self.retranslateUi(MyCharacters)
        QtCore.QMetaObject.connectSlotsByName(MyCharacters)

    def retranslateUi(self, MyCharacters):
        _translate = QtCore.QCoreApplication.translate
        MyCharacters.setWindowTitle(_translate("MyCharacters", "Form"))
        i = 1
        for characterButton in self.Characters:
            characterButton.setText(_translate("MyCharacters", f"Character {i}"))
            i += 1

