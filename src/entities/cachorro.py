from entities.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def to_dict(self):
        return {
            "tipo": "Cachorro",
            "nome": self.nome,
            "idade": self.idade,
            "raca": self.raca
        }

    @staticmethod
    def from_dict(data):
        return Cachorro(data["nome"], data["idade"], data["raca"])

    def __str__(self):
        return f"Cachorro(nome={self.nome}, idade={self.idade}, raca={self.raca})"