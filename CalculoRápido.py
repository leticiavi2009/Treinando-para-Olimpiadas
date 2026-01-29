S = int(input())
A = int(input())
B = int(input())
cont = 0
var = 0
for i in range(A, B + 1): #coloquei i dentro do intervalo entre A e B
    var = 0
    for j in str(i):# coloquei j para percorrer cada caractere da string
        var += int(j) #transformei o j - que é um caractere - em um inteiro para eu conseguir somar     
    if var == S: # verifiquei se a soma dos algarismos são iguais a S
            cont+=1 # se sim, coloquei para aumentar em um dígito a quantidade de numeros em que seus algarismos são iguais a S   
       
#a identação desse código é de extrema importância!!!
       

print(cont)

        
    



