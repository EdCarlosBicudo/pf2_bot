import openpyxl
from models import database
from models.Talento import Talento, Tipo, TipoTalento

FILE = "data/talentos.xlsx"


def create_tables():
    with database.database as db:
        db.create_tables([Talento, Tipo, TipoTalento])


def load_file():
    file = openpyxl.load_workbook(FILE, data_only=True)
    data = []
    sheets = ["gerais", "classes", "ancestralidade"]
    for s in sheets:
        sheet = file[s]

        for line in sheet[f"A1:K{sheet.max_row}"]:
            talento = {}
            talento["nome"] = line[0].value.title()
            talento["nivel"] = line[1].value
            talento["acao"] = line[2].value
            talento["pre_requisito"] = line[3].value
            talento["descricao"] = line[4].value
            talento["tipo"] = []

            for i in range(5, 11):
                if tipo := line[i].value:
                    talento["tipo"].append(tipo)
            data.append(talento)
    return data


def setup_tipo_talento(data):
    tipos = set()
    for talento in data:
        tipos.update(talento["tipo"])

    with database.database.atomic():
        for tipo in tipos:
            Tipo.create(nome=tipo)


def setup_talentos(data):

    with database.database.atomic():
        for talento in data:
            t = Talento.create(nome=talento["nome"],
                               nivel=talento["nivel"],
                               acao=talento["acao"],
                               pre_requisito=talento["pre_requisito"],
                               descricao=talento["descricao"])

            for tipo in talento["tipo"]:
                aux = Tipo.select().where(Tipo.nome == tipo).get()
                t.tipos.add(aux)
            t.save()


def setup():
    create_tables()
    data = load_file()
    setup_tipo_talento(data)
    setup_talentos(data)


if __name__ == '__main__':
    setup()
