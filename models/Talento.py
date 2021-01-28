from peewee import CharField, IntegerField, ManyToManyField
from models import BaseModel


class Talento(BaseModel.BaseModel):
    nome = CharField()
    nivel = IntegerField()
    acao = CharField(null=True)
    pre_requisito = CharField(null=True)
    descricao = CharField()


class Tipo(BaseModel.BaseModel):
    nome = CharField(unique=True)
    talentos = ManyToManyField(Talento, backref="tipos")


TipoTalento = Tipo.talentos.get_through_model()
