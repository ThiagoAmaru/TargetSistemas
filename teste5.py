lista = []
lista2 = []
variavel = input("Digite aqui: ")
for x in variavel:
    lista.append(x)

indice = (len(lista)-1)


while indice > -1:
    lista2.append(lista[indice])
    indice -= 1

print(lista2)