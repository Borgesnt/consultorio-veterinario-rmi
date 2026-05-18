from entities.consulta import Consulta
from entities.estoque import Estoque
from entities.item_estoque import ItemEstoque
from utils.serializer import animal_from_dict

class ServicoClinicaVeterinaria:
    def __init__(self):
        self.animais = []
        self.consultas = []
        self.estoque = Estoque()

    def cadastrar_animal(self, args):
        animal = animal_from_dict(args)
        self.animais.append(animal)
        return f"Animal cadastrado: {animal}"

    def listar_animais(self, args=None):
        if len(self.animais) == 0:
            return "Nenhum animal cadastrado."
        return [a.to_dict() for a in self.animais]

    def registrar_consulta(self, args):
        consulta = Consulta.from_dict(args)
        self.consultas.append(consulta)
        return f"Consulta registrada: {consulta}"

    def listar_consultas(self, args=None):
        if len(self.consultas) == 0:
            return "Nenhuma consulta registrada."
        return [c.to_dict() for c in self.consultas]

    def adicionar_item_estoque(self, args):
        item = ItemEstoque.from_dict(args)
        self.estoque.adicionar_item(item)
        return f"Item adicionado ao estoque: {item}"

    def consultar_estoque(self, args=None):
        itens = self.estoque.listar_itens()
        if len(itens) == 0:
            return "Estoque vazio."
        return [i.to_dict() for i in itens]