### Error Types ###

# SyntaxError
# print "¡Hola Comunidad!" # Descomentar Error
print ("¡Hola Comunidad!")

# NameError
language = "Spanish" # comentar Error
print(language)

#IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #Descomentar para Error

# ModuleNotFoundError
# import maths # Descomentar para Error
import math

# AttributeError
#print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre" : "Brais", "Apellido": "Moure", "Edad":35 , 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error


# TypeError
#print(my_list["Nombre"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para Error
print(4/2)