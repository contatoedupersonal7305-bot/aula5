clientes = ["Ana", "Hugo", "Marta", "Pedro"]
aluno1 = {"nome": "Ana", "nota": 8, "cel": "1178781234"}

clientes = [
    {"nome": "Ana", "cel": "1178781234", "empresa": "FIAT"},
    {"nome": "Pedro", "cel": "1167894944", "empresa": "HONDA"},
    {"nome": "Maria", "cel": "444444", "empresa": "SEBRAE"},
    {"nome": "Felipe", "cel": "555555", "empresa": "MICROSOFT"},
]

pergunta_emp = input("Qual empresa voce quer? ").upper()


for cliente in clientes:
    if cliente["empresa"] == pergunta_emp:
        print(cliente["nome"])

#Cadastrar novo cliente

print("--->Cadastrando um novo CLIENTE<---")
nome = input("Digite o nome do cliente: ")
celular = input("Digite o número de celular do cliente: ")
empresa = input("Digite a empresa do cliente: ")

novo_cliente = {
    "nome": nome,
    "cel": celular,
    "empresa": empresa,
}
clientes.append(novo_cliente)
print(clientes)

#Remover um Cliente

print("--->Removendo um cliente<---")
nome_clientes = input("Digite o nome do cliente que quer remover: ")
for cliente in clientes:
    if cliente["nome"] == nome_clientes:
        clientes.remove (cliente)
        break

print(clientes)
