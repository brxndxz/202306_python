#Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
#la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
#Por ejemplo, dada la siguiente lista:
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(lista):
    for i in lista:
        for key, value in i.items():
            print(f'{key} - {value}') 
iterate_dictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
def iterateDictionary2(key_name, lista):
    for i in lista:
        for key, value in i.items():
            if key == key_name:
                print(value)
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

