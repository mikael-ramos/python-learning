resposta = "S"
equipamento = ["eq1","eq3","eq4","eq2","eq5"]
serial = [11,2222,33,2727,99]
valor = [135.98,135.98,135.98,135.98,135.98]
departamento = ["TI","TI","TI","TI","TI"]

while resposta == "S":
    busca = input("Que item você deseja deletar do iventario ?")
    for elementos in range(0,len(equipamento),1):
        if busca == equipamento[elementos]:
            del equipamento[elementos]
            print("Item deletado")
            break

    resposta = input("Deseja deletar mais alguma coisa ?").upper()



