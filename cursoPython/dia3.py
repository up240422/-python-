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

print(f"Pendiente (m): {m}")
print(f"Intersección con el eje y (b): (0, {b})")
print(f"Intersección con el eje x: ({interseccion_x}, 0)")


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

























 





