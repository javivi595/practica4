#P4E3 JAVIER DURAN Calcula el area de un rectangulo o de un cuadrado segun se pida

opcion=input("Introduce si quieres calcular el area de un cuadrado o un rectangulo:")
if opcion=="cuadrado":
    lado=int(input("Introduce cuanto mide el costado: "))
    print("El area del cuadrado es {}".format(lado**2))
elif opcion=="rectangulo":
    base, altura=map(int,input("Introduce la base y la altura: ").strip().split())
    print("El area del rectangulo es {}".format(base*altura))
else:
    print("Opcion incorrecta")