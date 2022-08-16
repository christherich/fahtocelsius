from __future__ import division
from ast import If

# INPUT
fahrenheit = input('Fahrenheit: ')

# VALUES
minus = 32
division = 1.8
fahrenheit = int(fahrenheit)
fahresult1 = (fahrenheit - minus)

# RESULT
fahresult2 = (fahresult1 / division)

# PRINT
print(fahresult2)

val = 'i'

for val in "string":
    if val == "i":
        break
################################################################################

# INPUT
celsius = input('Celsius: ')

# CONVERT INPUT TO INT
celsius = int(celsius)

# VALUES
celsiusmultiplier = 1.8
celsiusaddition = 32

# RESULT
celsiusresult = celsius * celsiusmultiplier + celsiusaddition

# PRINT
print(celsiusresult)
