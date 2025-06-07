# Sistema de Gerenciamento de Eventos Universitários

# Lista para armazenar eventos
eventos = []

def cadastrar_evento():
    nome = input("Nome do evento: ")
    data = input("Data do evento (DD/MM/AAAA): ")
    descricao = input("Descrição do evento: ")
    max_participantes = int(input("Número máximo de participantes: "))
    evento = {
        "nome": nome,
        "data": data,
        "descricao": descricao,
        "max_participantes": max_participantes,
        "inscritos": []
    }
    eventos.append(evento)
    print("Evento cadastrado com sucesso!")

def listar_eventos():
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    for i, evento in enumerate(eventos, start=1):
        vagas_restantes = evento["max_participantes"] - len(evento["inscritos"])
        print(f"{i}. {evento['nome']} - {evento['data']} (Vagas restantes: {vagas_restantes})")
        print(f"Descrição: {evento['descricao']}")

def atualizar_evento():
    listar_eventos()
    escolha = int(input("Selecione o número do evento para atualizar: ")) - 1
    if escolha < 0 or escolha >= len(eventos):
        print("Evento inválido.")
        return
    print("O que deseja atualizar?")
    print("1. Nome")
    print("2. Data")
    print("3. Descrição")
    print("4. Número máximo de participantes")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        eventos[escolha]["nome"] = input("Novo nome: ")
    elif opcao == 2:
        eventos[escolha]["data"] = input("Nova data (DD/MM/AAAA): ")
    elif opcao == 3:
        eventos[escolha]["descricao"] = input("Nova descrição: ")
    elif opcao == 4:
        eventos[escolha]["max_participantes"] = int(input("Novo número máximo de participantes: "))
    else:
        print("Opção inválida.")
        return
    print("Evento atualizado com sucesso!")

def inscrever_no_evento():
    listar_eventos()
    escolha = int(input("Selecione o número do evento para se inscrever: ")) - 1
    if escolha < 0 or escolha >= len(eventos):
        print("Evento inválido.")
        return
    evento = eventos[escolha]
    if len(evento["inscritos"]) >= evento["max_participantes"]:
        print("Evento lotado.")
        return
    nome_participante = input("Seu nome: ")
    evento["inscritos"].append(nome_participante)
    print("Inscrição realizada com sucesso!")

def visualizar_inscritos():
    listar_eventos()
    escolha = int(input("Selecione o número do evento para visualizar os inscritos: ")) - 1
    if escolha < 0 or escolha >= len(eventos):
        print("Evento inválido.")
        return
    evento = eventos[escolha]
    print(f"Inscritos no evento '{evento['nome']}':")
    if not evento["inscritos"]:
        print("Nenhum inscrito até o momento.")
    else:
        for participante in evento["inscritos"]:
            print(f"- {participante}")

def excluir_evento():
    listar_eventos()
    escolha = int(input("Selecione o número do evento para excluir: ")) - 1
    if escolha < 0 or escolha >= len(eventos):
        print("Evento inválido.")
        return
    eventos.pop(escolha)
    print("Evento excluído com sucesso!")

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Eventos ---")
        print("1. Cadastrar Evento")
        print("2. Listar Eventos")
        print("3. Atualizar Evento")
        print("4. Inscrever-se em Evento")
        print("5. Visualizar Inscritos")
        print("6. Excluir Evento")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_evento()
        elif escolha == "2":
            listar_eventos()
        elif escolha == "3":
            atualizar_evento()
        elif escolha == "4":
            inscrever_no_evento()
        elif escolha == "5":
            visualizar_inscritos()
        elif escolha == "6":
            excluir_evento()
        elif escolha == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
