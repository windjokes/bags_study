# *.* coding=utf-8  *.*

"""
Peewee中文文档
http://blog.csdn.net/amoscn/article/details/74529133
本部分由-创建数据库-创建表-操作表-增删改查-其他组成
"""

# 1.创建数据库

from peewee import *

# 如果这边没有这个数据库会自动创建
db = SqliteDatabase('people.db')

# 2.创建表

# 首先来定义表单

class Person(Model):


    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db #  这个模型使用 "people.db"数据库
# 请注意我们命名我们的模型为Persopn而不是People。
# 这个惯例你应该遵守-虽然这张表包含许多people，我
# 们总是使用单数形式命名该类。

class Pet(Model):


    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # 这个模型使用"people.db"数据库

# 3.操作表

# 3-1连接与关闭

db.connect()
db.close()

# 3-2增(存储数据)

# save()增加数据
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save() # bob 现在被存储在数据库内

#create()增加数据
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat') #这个后来被删掉了
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# 3-3删
# .delete_instance()引用删除函数
herb_mittens.delete_instance()#它拥有伟大的一生，就是删死了

# 3-4改

# peewee直接调用类方法的方法，用.save()的方式修改修改
grandma.name = 'Grandma L.'
grandma.save()  #  在数据库更新Grandma的名字

#Bob叔叔发现太多的动物死在了Herb家，所以他领养了Fido： --非常生动的改动例子
herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido # 为了更清晰重命名我们的变量

# 3-5查

#让我们从数据库来检索Grandma的记录。为了从数据库获取单条记录，使用SelectQuery.get():
grandma = Person.select().where(Person.name == 'Grandma L.').get()

#我们也可以使用等效的简写Model.get()：
grandma = Person.get(Person.name == 'Grandma L.')

#让我们列出表内的所有人:
for person in Person.select():
    print person.name, person.is_relative
#Bob True
#Grandma L. True
#Herb False
#如果只写person就会返回<__main__.Person object at 0x02D2EE70>

#让我们列出所有的猫和他们的主人的名字:
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print pet.name, pet.owner.name
#Kitty Bob
#Mittens Jr Herb

#我们可以通过选择Pet和Person并且添加一个join来避免额外的查询。
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))
for pet in query:
    print pet.name, pet.owner.name
#Kitty Bob
#Mittens Jr Herb


# 3-6其他



































