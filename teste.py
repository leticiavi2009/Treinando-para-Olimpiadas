def ler_entrada():
    with open("notas.in") as notas:
        dados = notas.readlines()


    for i in range(len(dados)):
        dados[i] = dados[i].rstrip("\n").split()
        for j in range(1, len[dados]):
            dados[i][j] = int(dados[i][j])  
    return dados

ler_entrada()