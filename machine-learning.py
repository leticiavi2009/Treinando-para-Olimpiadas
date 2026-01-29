N = int(input())
dicionario = {}
contagem = {} #foi usado o simbolo de dicionario para contar qual vai ser a maior quantidade de vezes que uma palavra vai ser mencionada
for _ in range(N):
    entrada = input().split() # separei geral, adiciona automaticamente numa lista
    topico = entrada[0] #coloquei que a primeira palavra separada vai ser o topico
    qnt_palavras = entrada[1] #coloquei que o numero vai ser a quantidade de palavras
    palavras = entrada[2:] #a partir do 2 a frente vai ser as palavras presente no topico

    contagem[topico] = 0 #aqui esta referindo que a contagem vai ser do topico

    for palavra in palavras:
        dicionario [palavra] = topico #palavra pertence ao topico -->palavra =chave, topico =valor-->palavra x pertence ao topico y

_ =int(input())#pega o numero e descarta, n sei se pode isso!!!
artigo = input().split()#separa as palavras 

for palavra in artigo: #pega cada palavra do artigo e verifica
    if palavra in dicionario:#verifica se cada uma das palavras esta no dicionario
        topico = dicionario[palavra]#busca: dado a palavra, descobre qual é o tópico dela
        contagem[topico] += 1#parei aqui, ver como funciona na pratica

maior = -1
topico_do_artigo =" "

for topico,qtd in contagem.items():
    if qtd > maior or (qtd == maior and topico < topico_do_artigo) :
        maior = qtd
    topico_do_artigo = topico

print(topico_do_artigo)
print(dicionario.items())