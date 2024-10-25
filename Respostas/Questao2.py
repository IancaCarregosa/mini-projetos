a = str(input("digite uma frase: "))
ver = a.upper().count('A')
if ver>0:
    print(f"há um total de {ver} 'A's nessa frase!")
else:
    print('não há letra A nessa frase')