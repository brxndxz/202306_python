#Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas,
#imprima el nombre de cada clave junto con el tamaño de su lista, 
#y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for key, value in dict.items():
        print(f"{len(value)}{key}")
        for i in range(0, len(value)):
            print(value[i])
printInfo(dojo)

