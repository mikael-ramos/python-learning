tabuada = int(input("Digite um numero para exbir a tabuada: "))
print("Tabuada numero ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str(tabuada*valor))