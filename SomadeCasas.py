lista = []
lista2 = []
def casas():
    quantidadeCasas = int(input())
    for i in range(quantidadeCasas):
        lista.append(int(input()))
    num = lista[-1]
    for i in range(len(lista)):
        if num == lista[i] + lista[i+1]:
            lista2.append(lista[i])
            lista2.append(lista[i+1])
print(lista2)
