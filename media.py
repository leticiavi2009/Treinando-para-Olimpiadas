def media_N_valores():
    quant_valores = len(notas)
    soma = 0
    for i in range(quant_valores):
        soma += notas[i] # aqui o i vai para LISTA DE NOTAS nao para o range
    media = soma / quant_valores
    return media

media = media_N_valores()
notas = list(map(int, input().split()))
print(media)