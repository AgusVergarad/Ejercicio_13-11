numeros = []

print("Ingresa 10 numeros:")

for i in range(10):

  num = float(input(f"Numero {i + 1}: "))

  numeros.append(num)



opcion = ""
while opcion != "3":

  print("MENU DE ORDENAMIENTO")
  print("1. Mostrar de menor a mayor")
  print("2. Mostrar de mayor a menor")
  print("3. Salir")

  opcion = input("Elige una opcion (1, 2 o 3): ")

  if opcion == "1":
    ordenados_menor_mayor = sorted(numeros)

    print("Lista ordenada de menor a mayor:")
    print(ordenados_menor_mayor)