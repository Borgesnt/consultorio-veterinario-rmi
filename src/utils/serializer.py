from entities.cachorro import Cachorro
from entities.gato import Gato
from entities.coelho import Coelho
from entities.animal import Animal

def animal_from_dict(data):
    tipo = data.get("tipo")

    if tipo == "Cachorro":
        return Cachorro.from_dict(data)
    if tipo == "Gato":
        return Gato.from_dict(data)
    if tipo == "Coelho":
        return Coelho.from_dict(data)

    return Animal.from_dict(data)