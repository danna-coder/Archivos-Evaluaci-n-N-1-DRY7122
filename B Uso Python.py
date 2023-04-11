#print("Evaluación N°1 Programación y Redes Virtualizadas - Dannae Quidenao Adasme"
#nombre = input ("Ingrese su nombre: ")
#apellido = input ("Ingrese su apellido: ")
#codigo = input ("Ingrese su codigo y seccion: ")
#sede = input ("Ingrese su sede: ")
#
#print (nombre,apellido,codigo,sede)

aclNum =int(input("Ingrese el valor a consultar de ACL: "))
if (aclNum >=1 and aclNum <=99):
    print("Esta es una ACL estandar")
elif (aclNum >=100 and aclNum <=199):
    print ("Esta es una ACL extendida")
else:
    print ("Esta no es una ACL estandar ni extendida")
