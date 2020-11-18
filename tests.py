import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from bson import ObjectId
from intro import Ui_MainWindow
from newcharacters import Ui_Newcharacters
from setting import Ui_Setting
from search import Ui_SearchUser
from mycharacters import Ui_MyCharacters
from character import Ui_character
from randomcharacter import Ui_RandomCharacter
from mongoengine import *
from mini_window import NoUser, UserRegistered, WrongPassword
from mongodb import User, Characters
import random
connect('database', host='mongodb+srv://Tiris:Et21121982@cluster1.rzt5y.\
mongodb.net/database?retryWrites=true&w=majority')
result = None
char = None
list_of_characters = None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.open_new_char = NewcharWindow()
        self.open_search_user = SearchUsers()
        self.open_setting = SettingWindow()
        self.open_my_char = MycharactersWindow()
        self.open_wrong_pass = WrongPassword()
        self.open_random_character = RandomCharacter()
        self.open_user_registered = UserRegistered()
        self.setupUi(self)
        self.sign.clicked.connect(self.sign_in)
        self.newchar.clicked.connect(self.open_new_char_window)
        self.setting.clicked.connect(self.open_setting_window)
        self.mychar.clicked.connect(self.open_my_char_window)
        self.search_user.clicked.connect(self.open_search_user_window)
        self.randomchar.clicked.connect(self.open_random_character_window)
        self.security = 0

    def sign_in(self):
        login = self.logedit.text()
        password = self.passedit.text()
        global result
        result = list(User.objects(log_user=login))
        if not result:
            new_user = User(log_user=login, pass_user=password).save()
            self.user.setText(login)
            self.security = 1
            result = list(User.objects(log_user=login))
            self.open_user_registered.show()
        else:
            if password == result[0].pass_user:
                self.user.setText(login)
                self.security = 1
                if result[0].photo:
                    photo = result[0].photo.read()
                    f = open('avatar.png', 'wb')
                    f.write(photo)
                    f.close()
                    self.pixmap = QPixmap('avatar.png')
                    self.avatar.setScaledContents(True)
                    self.avatar.setPixmap(self.pixmap)
            else:
                self.open_wrong_pass.show()

    def open_random_character_window(self):
        if self.security == 1:
            self.open_random_character.show()

    def open_search_user_window(self):
        if self.security == 1:
            self.open_search_user.show()

    def open_new_char_window(self):
        if self.security == 1:
            self.open_new_char.show()

    def open_setting_window(self):
        if self.security == 1:
            self.open_setting.show()

    def open_my_char_window(self):
        if self.security == 1:
            self.open_my_char.show()


class NewcharWindow(QWidget, Ui_Newcharacters):
    def __init__(self):
        super(NewcharWindow, self).__init__()
        self.setupUi(self)
        self.share_question = 1
        self.saves.clicked.connect(self.created_characters)
        self.choose.clicked.connect(self.choose_the_picture)
        self.shows.toggle()
        self.shows.stateChanged.connect(self.share_quation_function)
        self.proverka = 0

    def share_quation_function(self, state):
        if state == Qt.Checked:
            self.share_question = 1
        else:
            self.share_question = 0

    def choose_the_picture(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.fname)
        self.imagechar.setScaledContents(True)
        self.imagechar.setPixmap(self.pixmap)
        self.proverka = 1

    def created_characters(self):
        name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        age = self.ageEdit.text()
        race = self.raceEdit.text()
        height = self.heightEdit.text()
        share = self.share_question
        weight = self.weightEdit.text()
        bio = self.textbio.toPlainText()
        appear = self.textapp.toPlainText()
        charact = self.textEdit_3.toPlainText()
        gender = self.gender.currentText()
        number = self.char_number.currentText()
        new_char = Characters(name_char=name, surname_char=surname, age_char=age, bio_char=bio, \
                              race_char=race, height_char=height, weight_char=weight, app_char=appear, \
                              char_char=charact, gender_char=gender, share_to_other=share).save()
        if self.proverka == 1:
            new_char.photo_char = self.fname
            new_char.save()
        global result
        if number == 'Character_1':
            result[0].character_1 = str(new_char.id)
        elif number == 'Character_2':
            result[0].character_2 = str(new_char.id)
        elif number == 'Character_3':
            result[0].character_3 = str(new_char.id)
        elif number == 'Character_4':
            result[0].character_4 = str(new_char.id)
        elif number == 'Character_5':
            result[0].character_5 = str(new_char.id)
        elif number == 'Character_6':
            result[0].character_6 = str(new_char.id)
        elif number == 'Character_7':
            result[0].character_7 = str(new_char.id)
        elif number == 'Character_8':
            result[0].character_8 = str(new_char.id)
        elif number == 'Character_9':
            result[0].character_9 = str(new_char.id)
        elif number == 'Character_10':
            result[0].character_10 = str(new_char.id)
        result[0].save()


class SettingWindow(QWidget, Ui_Setting):
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.proverka = 0
        self.setupUi(self)
        self.picture.clicked.connect(self.choose_the_picture)
        self.saves1.clicked.connect(self.change_setting)

    def choose_the_picture(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.fname)
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(self.pixmap)
        self.proverka = 1

    def change_setting(self):
        lastpass = self.lastpassedit.text()
        result[0].log_user = self.newlogEdit.text()
        result[0].gender = self.gender_user.currentText()
        result[0].phone = self.phoneedit.text()
        result[0].email = self.emailedit.text()
        result[0].age = self.ageusedit.text()
        result[0].country = self.contuseredit.text()
        result[0].about_me = self.textaboutme.toPlainText()
        if self.proverka == 1:
            result[0].photo = self.fname
        if lastpass == result[0].pass_user:
            result[0].pass_user = self.newpassedit.text()
        result[0].save()


class MycharactersWindow(QWidget, Ui_MyCharacters):
    def __init__(self):
        super(MycharactersWindow, self).__init__()
        self.setupUi(self)
        for characterButton in self.Characters:
            characterButton.clicked.connect(self.character)

    def character(self):
        sender = self.sender().text().lower()
        id_char = ''
        for i in range(1, 11):
            characters = 'character ' + str(i)
            if characters == sender:
                character_i = 'character_' + str(i)
                id_char = eval('result[0].{0}'.format(character_i))
        global char
        char = list(Characters.objects(_id=ObjectId(id_char)))
        self.open_character = Character()
        self.open_character.show()


class Character(QWidget, Ui_character):
    def __init__(self):
        global char
        super(Character, self).__init__()
        self.setupUi(self)
        self.fio.setText(char[0].name_char + ' ' + char[0].surname_char)
        self.age.setText(char[0].age_char)
        self.race.setText(char[0].race_char)
        self.gender.setText(char[0].gender_char)
        self.height.setText(char[0].height_char)
        self.weight.setText(char[0].weight_char)
        self.biography.setText(char[0].bio_char)
        self.appearance.setText(char[0].app_char)
        self.character1.setText(char[0].char_char)
        if char[0].photo_char:
            photo = char[0].photo_char.read()
            opener = open('photo_char.png', 'wb')
            opener.write(photo)
            opener.close()
            self.pixmap = QPixmap('photo_char.png')
            self.image.setScaledContents(True)
            self.image.setPixmap(self.pixmap)


class SearchUsers(QWidget, Ui_SearchUser):
    def __init__(self):
        super(SearchUsers, self).__init__()
        self.setupUi(self)
        self.no_user = NoUser()
        self.search.clicked.connect(self.search_user)

    def search_user(self):
        name_of_user = self.name_of_user.text()
        result = list(User.objects(log_user=name_of_user))
        if not result:
            self.no_user.show()
        else:
            self.login_user.setText(result[0].log_user)
            self.gender_user.setText(result[0].gender)
            self.phone_user.setText(result[0].phone)
            self.email_user.setText(result[0].email)
            self.age_user.setText(result[0].age)
            self.country_user.setText(result[0].country)
            self.about_user.setText(result[0].about_me)
            if result[0].photo:
                photo = result[0].photo.read()
                opener = open('photo_user.png', 'wb')
                opener.write(photo)
                opener.close()
                self.pixmap = QPixmap('photo_user.png')
                self.photo.setScaledContents(True)
                self.photo.setPixmap(self.pixmap)


class RandomCharacter(QWidget, Ui_RandomCharacter):
    def __init__(self):
        super(RandomCharacter, self).__init__()
        self.setupUi(self)
        global list_of_characters
        self.load.clicked.connect(self.change_index)

    def change_index(self):
        list_of_characters = list(Characters.objects(share_to_other=1))
        self.index = random.randint(0, len(list_of_characters) - 1)
        self.fio.setText(list_of_characters[self.index].name_char + ' ' + list_of_characters[self.index].surname_char)
        self.age.setText(list_of_characters[self.index].age_char)
        self.race.setText(list_of_characters[self.index].race_char)
        self.gender.setText(list_of_characters[self.index].gender_char)
        self.height.setText(list_of_characters[self.index].height_char)
        self.weight.setText(list_of_characters[self.index].weight_char)
        self.biography.setText(list_of_characters[self.index].bio_char)
        self.appearance.setText(list_of_characters[self.index].app_char)
        self.character1.setText(list_of_characters[self.index].char_char)
        photo = list_of_characters[self.index].photo_char.read()
        opener = open('photo_random_char.png', 'wb')
        opener.write(photo)
        opener.close()
        self.pixmap = QPixmap('photo_random_char.png')
        self.image.setScaledContents(True)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
