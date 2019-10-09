#P4E2 JAVIER DURAN Pide 5 numeros y imprime si estaban en orden, al reves, o desordenado


numeros=list(map(int,input("Introduce 5 numeros: ").strip().split()))
menmay=numeros[:]
menmay.sort()
maymen=numeros[:]
maymen.sort(reverse=True)
if numeros==menmay:
    print("Los numeros estan ordenados de menor a mayor")
elif numeros==maymen:
    print("Los numeros estan ordenados de mayor a menor")
else:
    print("Los numeros estan desordenados")