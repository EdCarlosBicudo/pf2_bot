from peewee import Model
from models import database


class BaseModel(Model):
    class Meta:
        database = database.database
