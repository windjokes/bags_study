# *.* coding=utf-8 *.*

from peewee import *

db =SqliteDatabase('people.db')

class Person(Model):


    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):


    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # 这个模型使用"people.db"数据库

db.connect()

#db.create_tables([Person,Pet])

from datetime import date

# from datetime import date
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# uncle_bob.save() # bob 现在被存储在数据库内

#grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
#
# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')


for i in Person.select():
    print i.name


db.close()