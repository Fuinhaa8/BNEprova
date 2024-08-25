#função pesquisar
def Pesquisar(vet, n):
    aux = 0
    for i in vet:
        aux += 1
        if n == i:
            print(f"O valor foi encontrado. Sua posição é: {aux}")
            return True
       
    print("O valor não foi encontrado na lista.")
    return False

#lista e o valor digitado pelo usuário
lista = [9, 7, 2, 16, 14, 5]

while True:
    num = int(input("Informe o número que deseja pesquisar no vetor: "))
    if Pesquisar(lista, num):
        break

     
   
