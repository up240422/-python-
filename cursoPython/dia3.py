# ejercico one

myAge = 18 

# exercie two 

myHeight = 1.75

# exercie three 

z = 4 + 3j 

# exercie four 

base = float(input("Ingresa El Valor: "))
altura = float(input("Ingresa El Valor: "))
area = 0.5 * base * altura

#  exercie five 

ladoA = float(input("ingresa el lado A:"))
ladoB = float(input("ingresa el lado B:"))
ladoC = float(input("ingresa el lado C:"))
perimiter = ladoA + ladoB + ladoC 
print("Tha perimiter is ", perimiter)

# exercie six 

longitud = float(input("ingresa la longitud:"))
ancho = float(input("ingresa la anchura:"))
area1 = longitud * ancho 
perimetro = 2 * (longitud + ancho)
print("la area es: ",area1)
print("El perimetro es: ", perimetro)

# exercie seven 

radio = float(input("Ingresa el radio:"))
pi = 3.14
area2 = pi * radio**2  
circunference = 2 * pi * radio


# Calcular la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2

m = 2  # Pendiente
b = -2 # Intersección con el eje y

# Calcular la intersección con el eje x
# y = mx + b => 0 = 2x - 2
# 0 = 2x - 2 => x = 1
interseccion_x = -b / m

print("Pendiente (m): {m}")
print("Intersección con el eje y (b): (0, {b})")
print("Intersección con el eje x: ({interseccion_x}, 0)")


# La pendiente es (m = y2-y1/x2-x1). Halla la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6, 10)
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calcular la pendiente (m)
m = (y2 - y1) / (x2 - x1)
print(f"Pendiente (m): {m}")
# Calcular la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distancia Euclidiana: {distancia}")

#11. Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar distintos valores de x y determina en qué valor de x y será 0
x = float(input("ingresa el valor de x: "))
y= x**2 + 6*x + 9
if  y == 0:
    print("y es igual: ", y)
else:
    print("y no es igual a 0")


# 12. Encuentra la longitud de 'python' y 'dragon' y haz una afirmación de comparación falsa

longitudPython = len("python")
longitudDragon = len("dragon")
print(longitudPython)
print(longitudDragon)

# 13. Utilice el operador and para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon
print("Ejercicio 13")
print('on' in "python" and 'on' in "dragon" )

# 14. Espero que este curso no esté lleno de jerga . Utilice el operador in para comprobar si hay jerga en la oración
print("Ejercicio 14")
print('jerga' in "Espero que este curso no esté lleno de jerga")

# 15. No hay "on" tanto en dragon como en python
print("Ejercicio 15")
print(not 'on' in "python" and 'on' in "dragon")

# 16. Encuentra la longitud del texto de Python y convierte el valor a flotante y conviértelo en cadena
print("Ejercicio 16")
lonPython = len("python")
print(float(lonPython))
print(type(float(lonPython)))
print(str(lonPython))
print(type(str(lonPython)))

# 17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo comprobar si un número es par o no con Python?
print("Ejercicio 17")
numero = int(input("ingresa un numero: ")) 
if numero % 2 == 0 :
    print("numero par")
else :
    print("numero impar")

# 18. Comprueba si la división del piso de 7 por 3 es igual al valor int convertido de 2,7.
print("Ejercicio 18")
print(7 // 3 == int(2.7)) 

# 19. Check if type of '10' is equal to type of 10
print("Ejercicio 19")
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print("Ejercicio 20")
print(int(9.8) == 10)

# 21. Escriba un script que solicite al usuario que ingrese horas y tarifa por hora. ¿Cómo calcular el salario de la persona?
print("Ejercicio 21")
hours = int(input("horas de trabajo: "))
tarifa = int(input("tarifa por hora"))
salario = hours * tarifa 
print("tu salario es de: ", salario)

# 22. Escriba un script que solicite al usuario que ingrese la cantidad de años. Calcule la cantidad de segundos que puede vivir una persona. Suponga que una persona puede vivir cien años.
print("Ejercicio 22")
years = int(input("Ingresa los years:"))
life = years * 31540000
print("tiempo de vida en segundos son: ", life)   

# 23. Write a Python script that displays the following table
print("Ejercicio 23")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")



















 





