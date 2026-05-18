class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {
            "tipo": "Animal",
            "nome": self.nome,
            "idade": self.idade
        }

    @staticmethod
    def from_dict(data):
        return Animal(data["nome"], data["idade"])

    def __str__(self):
        return f"Animal(nome={self.nome}, idade={self.idade})"