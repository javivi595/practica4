#P4E4 JAVIER DURAN Introduce 4 numeros y indica si el último numero es divisor de los demás

a, b, c , d=map(int,input("Introduce 4 numeros: ").strip().split())
if a%d==0 and b%d==0 and c%d==0:
    print("El numero {} es divisor de los demas numeros".format(d))
else:
    print("El numero {} no es divisor".format(d))