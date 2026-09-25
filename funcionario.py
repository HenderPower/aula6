clientes = [
    {"nome": "Pedro","Celular":"11966192259", "empresa": "Microsoft"}, 
    {"none": "Matheus", "Celular": "11977238900", "empresa": "Volksvagem"},
    {"none": "David", "Celular": "11902383221", "empresa": "Microsoft"},
    {"nome": "Paulo", "Celular": "11980390675", "empresa": "Chevrolet "}
]
for cliente in clientes:
    
    if cliente["empresa"] == "Microsoft":
        print(cliente)

    
    
nome = input("Qual o nome do novo cliente: ")
Celular = input("Número de celular: ")
empresa = input("Nome da empresa: ")

novo_cliente = {
    "nome": nome,
    "Celular": Celular,
    "empresa": empresa
    }
clientes.append(novo_cliente)
print(clientes)

#clientes.append ({"nome": nome, "Celular": Celular, "empresa": empresa})
#print(clientes)

    


    # Remover
print("---> Removendo um Cliente pelo Nome")
nome_cliente = input ("Digite o nome do Cliente para remove-lo: ")
for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove (cliente)
        break

print(clientes)