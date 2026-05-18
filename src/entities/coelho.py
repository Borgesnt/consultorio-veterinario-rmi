from entities.animal import Animal

class Coelho(Animal):
    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade)
        self.peso = peso

    def to_dict(self):
        return {
            "tipo": "Coelho",
            "nome": self.nome,
            "idade": self.idade,
            "peso": self.peso
        }

    @staticmethod
    def from_dict(data):
        return Coelho(data["nome"], data["idade"], data["peso"])

    def __str__(self):
        return f"Coelho(nome={self.nome}, idade={self.idade}, peso={self.peso})"