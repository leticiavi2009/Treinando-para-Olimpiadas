#CADERNO DE TAREFAS OBI-F 2023
#ESTANTE.PY
var1 = input()
var2= []
for i in var1:
    if i !=" ":
        if int(i)>=1:
            var2.append(int(i))
        
soma = var2[0]+var2[2]+var2[1]
var3 = soma%var2[3]
print(var3)
