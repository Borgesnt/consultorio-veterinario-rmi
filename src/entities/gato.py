from entities.animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def to_dict(self):
        return {
            "tipo": "Gato",
            "nome": self.nome,
            "idade": self.idade,
            "cor": self.cor
        }

    @staticmethod
    def from_dict(data):
        return Gato(data["nome"], data["idade"], data["cor"])

    def __str__(self):
        return f"Gato(nome={self.nome}, idade={self.idade}, cor={self.cor})"