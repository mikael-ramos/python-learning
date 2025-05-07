equipamentos = []
departamento = []
valor = []
serial = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Qual o nome do equipamento ? "))
    valor.append(float(input("Qual o valor do equipamento ? ")))
    serial.append(int(input("Qual é o nome serial do equipamento ? ")))
    departamento.append(input("Qual é o departamento ?"))
    resposta = input("Deseja continuar ? ").upper()


busca = input("Qual o item que você deseja procurar ? ")

for item in range(0,len(equipamentos)):
   
    if busca == equipamentos[item]:
        print("Aqui esta o equipamento que estava procurando")
        print("O equipamento é ", equipamentos[item])
        print("O serial do equipamento é ", serial[item])
        print("O valor do equipamento é ", valor[item])
    
    else:
        item = item + 1
