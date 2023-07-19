#Primero más longitud: crea una función que acepte una list
#y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
sum = 0
def primero_mas_longitud(list):
    sum = list[0] + len(list)
    return sum
print(primero_mas_longitud([1,2,3,4,5]))
