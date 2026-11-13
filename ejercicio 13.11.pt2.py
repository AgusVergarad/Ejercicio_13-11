
numeros = []
print("Ingresa 10 números:")

for i in range(10):
    num = float(input(f"Número {i + 1}: "))
    
print("MENÚ DE ORDENAMIENTO")
print("1. Mostrar de menor a mayor")
print("2. Mostrar de mayor a menor")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    ordenados_menor_mayor = sorted(numeros)
    print("Lista ordenada de menor a mayor:")
    print(ordenados_menor_mayor)

elif opcion == "2":
    ordenados_mayor_menor = sorted(numeros, reverse=True)
    print("Lista ordenada de mayor a menor:")
    print(ordenados_mayor_menor)

else:
    print("Opción no válida.")