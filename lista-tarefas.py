tarefas = [
    {"titulo": "Exercitar" , "Concluido": "Sim", "Prioridade": "Alta"},
    {"titulo": "Lutar", "Concluido": "Nao", "Prioridade": "Alta"},
    {"titulo": "Meditar", "Concluido": "Sim", "Prioridade": "Baixa"},
    {"titulo": "Orar" , "Concluido": "Sim", "Prioridade": "Alta"},
    {"titulo": "Ler" , "Concluido": "Nao", "Prioridade": "Baixa"},
    {"titulo": "Lição" , "Concluido": "Sim", "Prioridade": "Baixa" },
    {"titulo": "Estudar", "Concluido": "Nao", "Prioridade": "Alta"},
    {"titulo": "Trabalhar", "Concluido": "Sim", "Prioridade": "Alta"}
]

print("---> Mostrando todas as tarefas: <---")

for tarefa in tarefas:
        print(tarefa["titulo"]) 

print("---> Mostrar Tarefas Concluídas <---")

for tarefa in tarefas:
        if tarefa["Concluido"] == "Sim":
                print(tarefa["titulo"], "- Sim")

print("---> Mostrar tarefas Pendentes <---")
for tarefa in tarefas:
        if tarefa["Concluido"] == "Nao":
                print(tarefa["titulo"], "- Nao")

print("---> Mostrar tarefas por Prioridade Alta <---")
for tarefa in tarefas:
        if tarefa["Prioridade"] == "Alta":
                print(tarefa["titulo"], "- Alta")

print("---> Mostrar tarefas por Prioridade Baixa <---")
for tarefa in tarefas:
        if tarefa["Prioridade"] == "Baixa":
                print(tarefa["titulo"], "- Baixa")

print("---> Cadastrar Nova Tarefa")

nome_tarefa = input("Qual é a nova tarefa: ")
concluir_tarefa = "Nao"
prioridade_tarefa = input("Qual o nível de prioridade da tarefa? Baixa/Alta ")

nova_tarefa = {
    "titulo": nome_tarefa,
    "Concluido": concluir_tarefa,
    "Prioridade": prioridade_tarefa
}
tarefas.append(nova_tarefa)
print(tarefas)

print("---> Finalizar tarefa")
