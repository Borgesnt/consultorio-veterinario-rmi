# Sistema Clínica Veterinária — Trabalho 2 (Sistemas Distribuídos)

**Universidade Federal do Ceará — Campus Quixadá**  
**Disciplina:** Sistemas Distribuídos  
**Código:** QXD0043  
**Docente:** Antônio Rafael Braga  
**Discentes:** Alfredo Borges do Nascimento Neto | Gessyca de Oliveira Cunha  

**Trabalho 2:** Remote Method Invocation (RMI)  
**Tema:** Clínica Veterinária  
**Linguagem:** Python 3  
**Tecnologias:** Pyro5 (RMI), JSON, Protocolo Request/Reply, Multi-thread interno do Pyro5  

---

## Visão Geral do Projeto

Este projeto implementa um sistema distribuído baseado em uma **Clínica Veterinária**, utilizando comunicação Cliente-Servidor via **Invocação Remota de Método (RMI)**.

O objetivo principal é demonstrar conceitos de:

- Invocação Remota de Método (Remote Method Invocation)
- Protocolo Request/Reply (Requisição-Resposta)
- Passagem de parâmetros por valor (JSON)
- Passagem por referência (objeto remoto)
- Uso de entidades com herança e agregação
- Organização baseada no modelo apresentado no livro-texto (Seção 5.2)

---

## Pré-requisitos

- Python 3.8+ (recomendado Python 3.10+)

Verifique sua versão com:

```bash
python3 --version
```

---

## Configuração do Ambiente Virtual (venv)

> **IMPORTANTE:** Recomenda-se fortemente o uso de ambiente virtual para evitar conflitos de dependências.

### Criar o ambiente virtual

Na raiz do projeto:

```bash
python3 -m venv venv
```

### Ativar o ambiente virtual

**Linux / Mac:**

```bash
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

Após ativar, você verá o prefixo `(venv)` no terminal.

---

## Dependências

Este projeto utiliza a biblioteca **Pyro5** para implementação de RMI. Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Como Rodar o Projeto

> **IMPORTANTE:** Sempre execute os comandos a partir da raiz do projeto:
> ```
> consultorio-veterinario-rmi/
> ```
> E sempre utilize `PYTHONPATH=src` para que o Python reconheça a pasta `src/` como raiz dos imports.

---

## Estrutura do Projeto

```
src/
 ├── client/
 │   └── client_main.py
 ├── entities/
 │   ├── animal.py
 │   ├── cachorro.py
 │   ├── gato.py
 │   ├── coelho.py
 │   ├── consulta.py
 │   ├── item_estoque.py
 │   └── estoque.py
 ├── rmi/
 │   ├── message.py
 │   ├── remote_object_ref.py
 │   ├── requestor.py
 │   └── invoker.py
 ├── server/
 │   ├── servico_clinica.py
 │   └── server_main.py
 └── utils/
     └── serializer.py
```

---

## Entidades Implementadas

O sistema possui entidades que representam uma clínica veterinária, com os seguintes relacionamentos:

### Herança ("é-um")

- `Cachorro` é um `Animal`
- `Gato` é um `Animal`
- `Coelho` é um `Animal`

### Agregação ("tem-um")

- `Estoque` possui uma lista de `ItemEstoque`
- `Consulta` possui um animal associado (nome do animal)

---

## Serviço Remoto Implementado

O servidor disponibiliza o objeto remoto `ServicoClinicaVeterinaria` com os seguintes métodos remotos:

| Método | Descrição |
|---|---|
| `cadastrar_animal()` | Cadastra um novo animal na clínica |
| `listar_animais()` | Lista todos os animais cadastrados |
| `registrar_consulta()` | Registra uma nova consulta |
| `listar_consultas()` | Lista todas as consultas registradas |
| `adicionar_item_estoque()` | Adiciona um item ao estoque |
| `consultar_estoque()` | Exibe os itens disponíveis no estoque |

---

## Protocolo Request/Reply

A comunicação segue o modelo **Request/Reply** conforme a Seção 5.2 do livro-texto.

O **cliente** utiliza o método:

```
doOperation(remoteObjectRef, methodId, arguments)
```

O **servidor** utiliza:

```
getRequest()
sendReply()
```

### Formato das Mensagens

As mensagens são estruturadas em formato JSON (representação externa de dados), contendo:

- `objectReference`
- `methodId`
- `arguments`

### Observação sobre o Pyro5

O **Pyro5 realiza automaticamente a serialização e transmissão dos dados**, portanto o sistema não manipula `bytes` diretamente nem faz gerenciamento manual de sockets — conforme permitido pelo enunciado do trabalho.

---

## Como Executar

### Terminal 1 — Iniciar o Servidor RMI

Com o ambiente virtual ativado:

```bash
PYTHONPATH=src python3 -m server.server_main
```

O servidor exibirá uma URI semelhante a:

```
PYRO:vetclinic@localhost:XXXXX
```

Copie essa URI exatamente como exibida.

### Terminal 2 — Iniciar o Cliente RMI

Com o ambiente virtual ativado:

```bash
PYTHONPATH=src python3 -m client.client_main
```

Cole a URI exibida pelo servidor quando solicitado.

---

## Exemplo de Uso

No cliente, você pode:

- Cadastrar animais (Cachorro, Gato, Coelho)
- Listar animais cadastrados
- Registrar consultas
- Listar consultas
- Adicionar itens no estoque
- Consultar o estoque

---

## Conclusão

Este projeto atende ao enunciado do Trabalho 2 aplicando:

- Comunicação Cliente-Servidor via RMI
- Protocolo Request/Reply
- Representação externa de dados (JSON)
- Passagem por referência para objetos remotos (Proxy Pyro5)
- Passagem por valor para entidades enviadas pelo cliente
- Entidades com herança e agregação

---

## Autores

**Alfredo Borges do Nascimento Neto**  
**Gessyca de Oliveira Cunha**  
UFC — Campus Quixadá