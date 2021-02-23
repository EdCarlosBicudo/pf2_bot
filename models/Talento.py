from peewee import CharField, ForeignKeyField, IntegerField
from models import BaseModel


class Talento(BaseModel.BaseModel):
    nome = CharField()
    nivel = IntegerField()
    acao = CharField(null=True)
    pre_requisito = CharField(null=True)
    descricao = CharField()

    def __str__(self):
        text = f"*{self.nome}* - {self.nivel}\n"
        for traco in self.tracos:
            text += f"{traco.traco} "
        if self.pre_requisito:
            text += f"\n*Pré-Requisitos:* {self.pre_requisito}"

        aux = self.descricao.replace(r'\n', '\n')
        text += f"\n{aux}"
        return text


class Traco(BaseModel.BaseModel):
    nome = CharField(unique=True)

    def __str__(self):
        return self.nome


class TracoTalento(BaseModel.BaseModel):
    talento = ForeignKeyField(Talento, backref="tracos")
    traco = ForeignKeyField(Traco, backref="talentos")
