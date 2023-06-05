#Variables
#forma correcta, camel case
myvariable = "My string variable"
print (myvariable)

#forma correcta, snake case
my_int_variable = 25
print (my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = True
print (my_bool_variable)

#concatenacion
print (f"{myvariable}, {my_int_variable}, {my_bool_variable} ")

#Forma erronea, no podemos empezar a escribir el nombre de una variable con mayuscula
Myvariable = "My string variable, foma erronea"
print (Myvariable)

print(f"Este es el valor de: {my_bool_variable}")

#Funciones del sistema
print(len(my_int_to_str_variable)) #funcion len(), cuanta los caracteres de una cadena. incluyendo los espacios

#variables en una sola linea | Cuidado con abusar de esta sintaxis
name, subname, alias, edad = "Mi nombre es Braily", "Mi apellido es Roman ", "Braulioo", 17

print(f"Mi nombre es {name}{subname}, pero la gente tiene la mala gana de decirme {alias}, mi edad actualmente es de {edad}")
print(type(edad))

"""
name = input("Cual es tu nombre: ")
edad = (input("Que edad tienes: "))

print(name)
print(edad) 
"""
#Cambiamos su tipo
name = 17
edad = "Braily"
print (name)
print (edad)

#¿Forzando el tipo?
dirreccion: str = "Calle mano tavarez justo"
print(type(dirreccion))
dirreccion = 20
print(type(dirreccion))

