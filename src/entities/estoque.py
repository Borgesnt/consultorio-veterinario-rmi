from entities.item_estoque import ItemEstoque

class Estoque:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: ItemEstoque):
        for i in self.itens:
            if i.nome.lower() == item.nome.lower():
                i.quantidade += item.quantidade
                return
        self.itens.append(item)

    def listar_itens(self):
        return self.itens

    def to_dict(self):
        return {
            "itens": [item.to_dict() for item in self.itens]
        }

    def __str__(self):
        if len(self.itens) == 0:
            return "Estoque vazio"
        return "\n".join(str(i) for i in self.itens)