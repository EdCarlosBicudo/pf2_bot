from peewee import CharField, IntegerField, ManyToManyField
from models import BaseModel

class Talento(BaseModel):
    nome = CharField()
    nivel = IntegerField()
    acao = CharField()
    pre_requisito = CharField()
    descricao = CharField()

class TipoTalento(BaseModel):
    nome = CharField(unique = True)
    talentos = ManyToManyField(Talento, backref="talentos")
