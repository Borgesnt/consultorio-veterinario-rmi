from rmi.remote_object_ref import RemoteObjectRef
from rmi.requestor import Requestor

def menu():
    print("\n====== CLIENTE - CLÍNICA VETERINÁRIA (RMI) ======")
    print("1 - Cadastrar Animal")
    print("2 - Listar Animais")
    print("3 - Registrar Consulta")
    print("4 - Listar Consultas")
    print("5 - Adicionar Item no Estoque")
    print("6 - Consultar Estoque")
    print("0 - Sair")
    return input("Escolha: ")

def cadastrar_animal(req, remote_ref):
    tipo = input("Tipo (Cachorro/Gato/Coelho): ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if tipo == "Cachorro":
        raca = input("Raça: ")
        args = {"tipo": "Cachorro", "nome": nome, "idade": idade, "raca": raca}
    elif tipo == "Gato":
        cor = input("Cor: ")
        args = {"tipo": "Gato", "nome": nome, "idade": idade, "cor": cor}
    elif tipo == "Coelho":
        peso = float(input("Peso: "))
        args = {"tipo": "Coelho", "nome": nome, "idade": idade, "peso": peso}
    else:
        print("Tipo inválido.")
        return

    reply = req.doOperation(remote_ref, "cadastrar_animal", args)
    print("Resposta:", reply)

def listar_animais(req, remote_ref):
    reply = req.doOperation(remote_ref, "listar_animais", {})
    print("Resposta:", reply)

def registrar_consulta(req, remote_ref):
    nome_animal = input("Nome do animal: ")
    data = input("Data (YYYY-MM-DD): ")
    motivo = input("Motivo: ")

    args = {"nome_animal": nome_animal, "data": data, "motivo": motivo}

    reply = req.doOperation(remote_ref, "registrar_consulta", args)
    print("Resposta:", reply)

def listar_consultas(req, remote_ref):
    reply = req.doOperation(remote_ref, "listar_consultas", {})
    print("Resposta:", reply)

def adicionar_item(req, remote_ref):
    nome = input("Nome do item: ")
    quantidade = int(input("Quantidade: "))

    args = {"nome": nome, "quantidade": quantidade}

    reply = req.doOperation(remote_ref, "adicionar_item_estoque", args)
    print("Resposta:", reply)

def consultar_estoque(req, remote_ref):
    reply = req.doOperation(remote_ref, "consultar_estoque", {})
    print("Resposta:", reply)

def main():
    print("======================================")
    print("CLIENTE RMI - CLÍNICA VETERINÁRIA")
    print("======================================")

    uri = input("Cole a URI do servidor (ex: PYRO:vetclinic@localhost:XXXXX): ")
    remote_ref = RemoteObjectRef(uri, "ServicoClinicaVeterinaria")

    requestor = Requestor()

    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_animal(requestor, remote_ref)
        elif opcao == "2":
            listar_animais(requestor, remote_ref)
        elif opcao == "3":
            registrar_consulta(requestor, remote_ref)
        elif opcao == "4":
            listar_consultas(requestor, remote_ref)
        elif opcao == "5":
            adicionar_item(requestor, remote_ref)
        elif opcao == "6":
            consultar_estoque(requestor, remote_ref)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()