#P4E1 JAVIER DURAN Recibe valores y indica cual de ellos es el menor y cual es mayor

numeros=list(map(int,input("Introduce 5 numeros: ").strip().split()))
print("El numero mayor es {} y el menor {}".format(max(numeros), min(numeros)))
