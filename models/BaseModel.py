from peewee import *

db = SqliteDatabase('pf2_bot.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db
