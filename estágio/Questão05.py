palavra = str(input('insira aqui a palavra para inverter: '))
palavraInvertida = ""  
for i in range(len(palavra) - 1, -1, -1):
    palavraInvertida += palavra[i]  
print(f"A palavra invertida fica assim: {palavraInvertida}")
