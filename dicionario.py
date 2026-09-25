
aluno = {"Nome": "Ana", "nota": 8, "celular": "11966192259" }


clientes = [
    {"nome": "Ana","celular":"11966192259", "empresa": "FIAT"}, 
    {"none": "Vinicius", "celular": "11977238900", "empresa": "Volksvagem"},
    {"none": "Arthur", "celular": "11902383221", "empresa": "Ferrari"},
    {"nome": "Rodrigo", "celular": "11980390675", "empresa": "Chevrolet "}
]

#print (clientes[1]["empresa"])

for cliente in clientes:
    if cliente["empresa"] == ["INTEL"]:
        print(cliente["nome"])
    
    # print (cliente["empresa"])