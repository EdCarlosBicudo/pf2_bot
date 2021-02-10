import openpyxl
from models import database
from models.Talento import Talento, Traco, TracoTalento

FILE = "data/talentos.xlsx"


def create_tables():
    with database.database as db:
        db.create_tables([Talento, Traco, TracoTalento])


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
            talento["tracos"] = []

            for i in range(5, 11):
                if traco := line[i].value:
                    talento["tracos"].append(traco)
            data.append(talento)
    return data


def setup_traco_talento(data):
    tracos = set()
    for talento in data:
        tracos.update(talento["tracos"])

    with database.database.atomic():
        for traco in tracos:
            Traco.create(nome=traco)


def setup_talentos(data):

    with database.database.atomic():
        for talento in data:
            t = Talento.create(nome=talento["nome"],
                               nivel=talento["nivel"],
                               acao=talento["acao"],
                               pre_requisito=talento["pre_requisito"],
                               descricao=talento["descricao"])
            for traco in talento["tracos"]:
                aux = Traco.select().where(Traco.nome == traco).get()
                TracoTalento.create(traco=aux, talento=t)


def setup():
    create_tables()
    data = load_file()
    setup_traco_talento(data)
    setup_talentos(data)


if __name__ == '__main__':
    setup()
