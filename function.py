#Funções são blocos de código que realizam tarefas específicas
#Permitem melhor organização e reutilização do código
#Imagine-as como cada peça que compõe um Quebra-Cabeça
#Programas bem escritos são compostos por Funções
lista = list(map(int, input().split()))
#definindo funções
def soma (x,y):  #dentro do parênteses ficam os parâmetros
    #o parâmetro é uma entrada
    return x + y
#soma = soma(int(input()), int(input()))#posso colocar o valor direto aqui tmb soma(1,1)
#print(soma)
#ou print(soma(int(input()),int(input())))
def media(lista):
    var = lista.pop(-1)
    return var
print(media(lista))
print(lista)



