### Python Package Manager ###

# PIP https://pypi.org

import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

import pandas # pip install pandas

# pip list

# pip install requests
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

#Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))