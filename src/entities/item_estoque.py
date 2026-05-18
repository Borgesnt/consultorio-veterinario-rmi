class ItemEstoque:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade
        }

    @staticmethod
    def from_dict(data):
        return ItemEstoque(data["nome"], data["quantidade"])

    def __str__(self):
        return f"ItemEstoque(nome={self.nome}, quantidade={self.quantidade})"