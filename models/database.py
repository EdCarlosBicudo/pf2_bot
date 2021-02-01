from peewee import SqliteDatabase

database = SqliteDatabase('pf2_bot.db', pragmas={'foreign_keys': 1})
