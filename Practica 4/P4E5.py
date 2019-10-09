#P4E5 JAVIER DURAN Devuelve la cantidad del billete mayor que se le puede 
#                  devolver en un cajero a un cliente
cliente=int(input("Introduce cuanto dinero quieres sacar:"))
if cliente%500==0:
    print("Se extraen {} billetes de 500".format(int(cliente/500)))
elif cliente%200==0:
    print("Se extraen {} billetes de 200".format(int(cliente/200)))
elif cliente%100==0:
    print("Se extraen {} billetes de 100".format(int(cliente/100)))
elif cliente%50==0:
    print("Se extraen {} billetes de 50".format(int(cliente/50)))
elif cliente%20==0:
    print("Se extraen {} billetes de 20".format(int(cliente/20)))
elif cliente%10==0:
    print("Se extraen {} billetes de 10".format(int(cliente/10)))
elif cliente%5==0:
    print("Se extraen {} billetes de 100".format(int(cliente/5)))
    