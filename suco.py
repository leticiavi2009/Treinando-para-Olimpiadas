#SUCO.PY
#o suco é somente contaminado se for 0 1
N = int(input())
if N>=1:
    for i in range(N):
        entrada_usuario = input()                       #para isso a gente coloca que o valor vai virar um inteiro e coloca o for para pegar cada nem e daí separa no .split
        A, B= (int(l) for l in entrada_usuario.split()) #aqui pega os dois valores e separa nas variáveis A e B e daí converte para inteiro,
        if A == 0 and B == 1:                           #tudo isso dentro de lista, se for [], se não ()
            N=N-1


print(N)