x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15 #Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
print(x)

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]["last_name"] = "Bryant" #Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print(estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes["fútbol"][0] = "Andrés" #En el directorio_deportes, cambia "Messi" por "Andrés".
print(directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z) #Cambia el valor 20 en z a 30.