class Consulta:
    def __init__(self, nome_animal, data, motivo):
        self.nome_animal = nome_animal
        self.data = data
        self.motivo = motivo

    def to_dict(self):
        return {
            "nome_animal": self.nome_animal,
            "data": self.data,
            "motivo": self.motivo
        }

    @staticmethod
    def from_dict(data):
        return Consulta(data["nome_animal"], data["data"], data["motivo"])

    def __str__(self):
        return f"Consulta(animal={self.nome_animal}, data={self.data}, motivo={self.motivo})"