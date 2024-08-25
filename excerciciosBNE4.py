#função para realizar o fatorial
def fat_num(fatorial):
  resultado = 1
  cont = 1
  while cont <= fatorial:
    resultado *= cont
    cont += 1
  return resultado 

#criando as variáveis 
fatorial = 2
dividendo = 224
Fat = 0

#iniciando um loop para fazer a conta e mostrar a sequência
print("FAT =", end=" ")
while fatorial <= 10:
  Fat = (dividendo / fat_num(fatorial) ) + Fat

  if fatorial == 10:
     print(f"({dividendo} / {fatorial}!) ")

  else:  
   print(f"({dividendo} / {fatorial}!) ", end="+ ")

  fatorial += 1
  dividendo += 4

#printando o a somatória
print("")
print(f"O somatório da sequência é: {Fat:.2f}")