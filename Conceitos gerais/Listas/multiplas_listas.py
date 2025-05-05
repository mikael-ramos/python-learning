equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Nome do equipamento: "))
    valores.append(input("Digite o valor: "))
    seriais.append(input("Digite o serial: "))
    departamentos.append(input("Digite o departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

#laço for usando o len()
for indice in range(0,len(equipamentos)):
    print("\nEquipamento", (indice + 1))
    print("Nome...........: ", equipamentos[indice])
    print("valor..........: ", valores[indice])
    print("serial.........: ", seriais[indice])
    print("departamento...: ", departamentos[indice])