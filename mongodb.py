from mongoengine import *


class User(DynamicDocument):
    log_user = StringField(required=True)
    pass_user = StringField(required=True)
    photo = ImageField()
    gender = StringField()
    phone = StringField()
    email = StringField()
    age = StringField()
    country = StringField()
    about_me = StringField()
    character_1 = StringField()
    character_2 = StringField()
    character_3 = StringField()
    character_4 = StringField()
    character_5 = StringField()
    character_6 = StringField()
    character_7 = StringField()
    character_8 = StringField()
    character_9 = StringField()
    character_10 = StringField()


class Characters(DynamicDocument):
    name_char = StringField(required=True)
    surname_char = StringField(required=True)
    age_char = StringField(required=True)
    race_char = StringField()
    share_to_other = IntField()
    height_char = StringField()
    weight_char = StringField()
    bio_char = StringField()
    app_char = StringField()
    char_char = StringField()
    gender_char = StringField()
    photo_char = ImageField()
