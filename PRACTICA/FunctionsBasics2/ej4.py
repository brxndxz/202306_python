#Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva 
#que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
#Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, 
#has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
def valores_mayores_que_el_segundo(list):
    list2 = []
    for i in list:
        if i > list[1]:
            list2.append(i)
    return list2
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))