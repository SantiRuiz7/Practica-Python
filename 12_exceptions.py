### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

#try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")

#try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: #Opcional
    #Se ejecuta si no se produce excepción
    print("La ejecución continúa correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")

#Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un error")
except TypeError:
    print("Se ha producido un error")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)