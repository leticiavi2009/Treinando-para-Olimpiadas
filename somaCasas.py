lista = []
lista2 = []
def casas():
    quantidadeCasas = int(input())
    for i in range(quantidadeCasas):
        lista.append(int(input()))
    num = lista[-1]
    soma = 0

    while soma != num:
        lista2.append(lista.pop(0))
        lista2.append(lista.pop(0))
        soma = lista2[0] + lista2[1]
        if soma != num:
            lista2.pop(0)
            soma = 0

      


casas()    
print(lista2[0],lista2[1])      
