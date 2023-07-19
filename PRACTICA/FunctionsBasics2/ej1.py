# crea una función que acepte un número como entrada.
#Devuelve una lista nueva que cuente de uno en uno, 
#desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown(p):
    x = []
    for i in range(p,-1,-1):
        x.append(i)
    return x
print(countdown(10))

