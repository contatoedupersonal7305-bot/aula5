tarefas = [
    {"titulo": "Estudar", "Concluida": "SIM", "Prioridade": "Alta"},
    {"titulo": "Ler", "Concluida": "NÃO", "Prioridade": "Baixa"},
    {"titulo": "Lavar Louça", "Concluida": "NÃO", "Prioridade": "Média"},
    {"titulo": "Cozinhar", "Concluida": "SIM", "Prioridade": "Média"},
]

def mostrar():
    print(tarefas)
def concluidas():
    for tarefa in tarefas:
        if tarefa["Concluida"] == "SIM":
            print(tarefa["titulo"], tarefa["Concluida"])
def pendentes():
    for tarefa in tarefas:
        if tarefa["Concluida"] == "NÃO":
            print(tarefa["titulo"], tarefa["Concluida"])
def prioridade():
    for tarefa in tarefas:
        if tarefa["Prioridade"] == "Alta":
            print(tarefa["titulo"], tarefa["Prioridade"])
    for tarefa in tarefas:
        if tarefa["Prioridade"] == "Média":
            print(tarefa["titulo"], tarefa["Prioridade"])
    for tarefa in tarefas:
        if tarefa["Prioridade"] == "Baixa":
            print(tarefa["titulo"],  tarefa["Prioridade"])
def cadastro():
    titulo = input("Digite o nome da Tarefa: ")
    concluida = input("Digite se foi Concluída: ")
    prioridade = input("Digite a Prioridade: ")
    
    nova_tarefa = {
        "titulo": titulo,
        "Concluida": concluida,
        "Prioridade": prioridade,
    }
    tarefas.append(nova_tarefa)
    print(tarefas)
def finalizar():
    if pergunta == 6:
        print("\n--- Tarefas Disponíveis ---")
    for tarefa in tarefas:
        print(tarefa["titulo"])
                
    tarefa_desejada = input("Qual tarefa deseja finalizar? ")
            
    for tarefa in tarefas:
        if tarefa["titulo"] == tarefa_desejada:
            tarefa["Concluida"] = "SIM"
            print(f"A tarefa '{tarefa_desejada}' foi finalizada com sucesso!")
def remover():
    print("\n--- Tarefas Disponíveis ---")
    for tarefa in tarefas:
        print(tarefa["titulo"])
    nome_clientes = input("Digite o nome da tarefa: ")
    for tarefa_removida in tarefas:
        if tarefa_removida["titulo"] == nome_clientes:
            tarefas.remove (tarefa_removida)
            print(tarefas)
            break

print("#Lista de Tarefas#")
print("1 - Mostrar todas as Tarefas")
print("2 - Mostrar Tarefas Concluídas")
print("3 - Mostrar Tarefas Pendentes")
print("4 - Mostrar Tarefas por Prioridade")
print("5 - Cadastrar Tarefa")
print("6 - Finalizar Tarefa")
print("7 - Remover Tarefa")
print("0 - Sair")

while True:
    pergunta = int(input("Qual opção deseja? "))

    if pergunta == 1:
        mostrar()
    elif pergunta == 2:
        concluidas()
    elif pergunta == 3:
        pendentes()
    elif pergunta == 4:
        prioridade()
    elif pergunta == 5:
        cadastro()
    elif pergunta == 6:
        finalizar()
    elif pergunta == 7:
        remover()
    elif pergunta == 0:
        print("Programa Finalizado! Até a Próxima...")
        break
    else:
        print("Opção Inválida, tente novamente")
        pergunta = int(input("Qual opção deseja? "))

        

