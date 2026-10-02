tarefas = [
    {"titulo": "Exercitar" , "Concluido": "Sim", "Prioridade": "Alta"},
    {"titulo": "Lutar", "Concluido": "Nao", "Prioridade": "Alta"},
    {"titulo": "Meditar", "Concluido": "Sim", "Prioridade": "Baixa"},
    {"titulo": "Orar" , "Concluido": "Sim", "Prioridade": "Alta"},
    {"titulo": "Ler" , "Concluido": "Nao", "Prioridade": "Baixa"},
    {"titulo": "Liçao" , "Concluido": "Sim", "Prioridade": "Baixa" },
    {"titulo": "Estudar", "Concluido": "Nao", "Prioridade": "Alta"},
    {"titulo": "Trabalhar", "Concluido": "Sim", "Prioridade": "Alta"} ]

def mostrar_tarefas():
    print("---> Mostrando todas as tarefas: <---")
    for tarefa in tarefas:
        print(tarefa)

def mostrar_tarefas_concluidas():
        print("---> Mostrar tarefas Concluídas <---")
        for tarefa in tarefas:
                if tarefa["Concluido"] == "Sim":
                        print(tarefa)
def mostrar_tarefas_pendentes():
    print("---> Mostrar tarefas Pendentes <---")
    for tarefa in tarefas:
        if tarefa["Concluido"] == "Nao":
            print(tarefa["titulo"])

def mostrar_tarefas_prioridade():
        print("---> Mostrar tarefas por Prioridade Alta <---")
        for tarefa in tarefas:
                if tarefa["Prioridade"] == "Alta":
                        print(tarefa)

        print("---> Mostrar tarefas por Prioridade Baixa <---")
        for tarefa in tarefas:
                if tarefa["Prioridade"] == "Baixa":
                        print(tarefa)

def cadastrar_tarefa():
    print("---> Cadastrar Nova Tarefa <---")
    nome_tarefa = input("Qual é a nova tarefa: ")
    concluir_tarefa = "Nao"
    prioridade_tarefa = input("Qual o nível de prioridade da tarefa? Baixa/Alta: ")

    nova_tarefa = {
        "titulo": nome_tarefa,
        "Concluido": concluir_tarefa,
        "Prioridade": prioridade_tarefa
    }
    tarefas.append(nova_tarefa)
    print("Nova tarefa cadastrada com sucesso!")

def finalizar_tarefa():
        print("---> Finalizar tarefa <---")
        nome_tarefa = input("Digite o nome da tarefa que deseja finalizar: ")

        for tarefa in tarefas:
                if tarefa["titulo"] == nome_tarefa:
                        tarefa["Concluido"] = "Sim"
                        print("Tarefa finalizada com sucesso!")
                                                
                        break
        else:
                        print("Tarefa não encontrada.")
while True:
    
    print("1 - Mostrar todas as tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas pendentes")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Cadastrar nova tarefa")
    print("6 - Finalizar tarefa")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
         mostrar_tarefas()
        
    elif opcao == "2":
         mostrar_tarefas_concluidas()

    elif opcao == "3":
         mostrar_tarefas_pendentes()

    elif opcao == "4":
        mostrar_tarefas_prioridade()

    elif opcao == "5":
        cadastrar_tarefa()

    elif opcao == "6":
        finalizar_tarefa()

    elif opcao == "7":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida")