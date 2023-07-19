#Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: 
#tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
#y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
list = []
def length_and_value(a, b):
    for i in range(a):
        list.append(b)
    return list
print(length_and_value(6,3))