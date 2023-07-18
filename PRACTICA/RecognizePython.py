# este es un comentario de una línea
"""
Este es
un comentario
de varias líneas
"""
#variable declaration
num1 = 42 #number
num2 = 2.3 #float
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tupla
print(type(fruit))#type check, imprimir en consola
print(pizza_toppings[1])#acceder a un valor de una lista
pizza_toppings.append('Mushrooms')#agregar a la lista
print(person['name'])#acceder a un valor del diccionario
person['name'] = 'George' #cambiar un valor del diccionario
person['eye_color'] = 'blue'#cambiar un valor del diccionario
print(fruit[2]) #acceder a un valor de una tupla

#if else condicional, imprimir algo
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#if elif else condicional, imprimir algo en consola
if (string) < 5:
    print("It's a short word!")
elif (string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#for empieza en 0 y termina en 5
for x in range(5):
    print(x)
#for empieza en 2 y termina en 5
for x in range(2,5):
    print(x)
#for empieza en 2, termina en 10 y se incrementa de a 3
for x in range(2,10,3):
    print(x)
#while empieza en 0 y va hasta 5
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()#borra el último elemento de una lista
pizza_toppings.pop(1)#borra el elemento del índice elegido

print(person)#imprimir del diccionario
person.pop('eye_color')#borrar del diccionario
print(person)#imprimir del diccionario

#for para recorrer una lista
for topping in pizza_toppings:
    if topping == 'Pepperoni':#condicional if
        continue#continua
    print('After 1st if statement')#imprime
    if topping == 'Olives':#if
        break#para el loop

def print_hello_ten_times():#declaración de la función
    for num in range(10):#for del 0 al 10
        print('Hello')#imprime en consola

print_hello_ten_times()#ejecuta la función

def print_hello_x_times(x):#declaración de la función con u parametro x
    for num in range(x):#for del 0 a la X
        print('Hello')#imprime 

print_hello_x_times(4)#se llama a la función con argumento igual a 4

def print_hello_x_or_ten_times(x = 10):#declaración de la función con un parametro x = 10
    for num in range(x): #for del 0 al x
        print('Hello')#imprimir en consola

print_hello_x_or_ten_times()#se llama a la función con valor 10
print_hello_x_or_ten_times(4)#se llama a la función con valor 4

# comment multiline
"""
Bonus section
"""

num3 = 72 #declaración de variable numerica
print(num3) #imprime una variable
#agregar al índice
# fruit[0] = 'cranberry'
#imprimir del diccionario 
# print(person['favorite_team']) 
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)