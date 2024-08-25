import math

altura = int(input("Informe a altura: "))

aresta = 133.2
area_base = ((aresta * aresta) * math.sqrt(3)) / 4
area_faces = ((aresta * altura) / 2) * 4

area_total = area_base + area_faces

print(f"O resultado da area total do triângulo é: {area_total:.2f}")

