#inserindo o nome e criando a lista
nome = str(input("Insira o seu nome: "))
num = len(nome)
lista = []

#inserindo os elementos na lista
for i in range(num):
    valores = int(input("Insira os elementos da primeira lista: "))
    lista.append(valores)

#a lista de forma ordenada de frente para trás
n = len(lista)

for i in range(n):
    for f in range(n - i - 1):
         if lista[f] > lista[f + 1]:
             lista[f], lista[f + 1] = lista[f + 1], lista[f]

print(f"A lista ordenada de frente para trás: {lista}")

#a lista de forma ordenada de trás para frente
for i in range(n):
    for f in range(n - i - 1):
         if lista[f] < lista[f + 1]:
             lista[f], lista[f + 1] = lista[f + 1], lista[f]

print(f"A lista ordenada de trás para frente: {lista}")