def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperaturas_celsius = list(map(int, input().split())) #(int, input().split()) fazendo só isso vc nao está pegando cada item dentro da lista
temperaturas_fahrenheit = list(map(celsius_para_fahrenheit,temperaturas_celsius)) #escreve assim porque passa uma lista e não um valor único
print(temperaturas_fahrenheit)