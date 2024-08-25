#iniciando as listas
lista1 = [] 
lista2 = [] 
lista_intercalada = [] 

#inserindo valores nas duas listas
for i in range(50):
    num = int(input("Insira os elementos da primeira lista: "))
    lista1.append(num)

print("")

for i in range(50):
    num = int(input("Insira os elemntos da segunda lista: "))
    lista2.append(num)

#lista intercalada
for i in range(50):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

print(f"\nLista intercalada: {lista_intercalada}\n")

#media da lista intercalada
soma = 0
for i in lista_intercalada:
    soma += i 
tamanho = len(lista_intercalada)

print(f"Média da soma dos valores da lista intercalada: {soma/tamanho}")