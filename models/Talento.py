from peewee import CharField, IntegerField, ManyToManyField
from models import BaseModel


class Talento(BaseModel.BaseModel):
    nome = CharField()
    nivel = IntegerField()
    acao = CharField(null=True)
    pre_requisito = CharField(null=True)
    descricao = CharField()

    def __str__(self):
        text = f"{self.nome}\n"
        if self.pre_requisito:
            text += f"Pré-Requisitos: {self.pre_requisito}\n"

        text += self.descricao
        return text


class Tipo(BaseModel.BaseModel):
    nome = CharField(unique=True)
    talentos = ManyToManyField(Talento, backref="tipos")


TipoTalento = Tipo.talentos.get_through_model()
