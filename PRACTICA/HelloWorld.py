# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")
# 2.
myname = "Brenda"
print("Hola, "+ myname)	# con un +
print("¡Hola,",myname,"!")	# con una coma
# 3.
name = 7
print("Hola", name )	# con una coma
#print("Hola " + name)	# con una +	-- este debería arrojar un error!
print("Hola " + str(name))	# con una +	-- este debería arrojar un error!
# 4.
fave_food1 = "milanesas"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1, fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f
#print(f"Amo comer {fave_food1} y {fave_food2}").upper()
varString = "esto es un string".upper()
print(varString)
