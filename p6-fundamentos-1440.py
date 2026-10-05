# marco morquecho 1440
# ==============================================================================
# ACTIVIDAD: P6 - Fundamentos de Python y Machine Learning
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. EJEMPLOS DE VARIABLES (Asignación básica)
# ------------------------------------------------------------------------------
# Ejemplo 1: Variable de texto (String)
nombre = "Carlos"
print("Nombre:", nombre)

# Ejemplo 2: Variable entera (Integer)
edad = 20
print("Edad:", edad)

# Ejemplo 3: Variable flotante (Float)
estatura = 1.75
print("Estatura:", estatura)


# ------------------------------------------------------------------------------
# 2. EJEMPLOS DE ASIGNACIÓN MULTIPLE DE VARIABLES
# ------------------------------------------------------------------------------
# Ejemplo 1: Asignar múltiples valores a múltiples variables
x, y, z = "Manzana", "Banana", "Cereza"
print("Frutas:", x, y, z)

# Ejemplo 2: Asignar un mismo valor a múltiples variables
a = b = c = "Machine Learning"
print("Valores iguales:", a, b, c)

# Ejemplo 3: Desempaquetar una lista en variables
frutas = ["Naranja", "Mango", "Uva"]
p, q, r = frutas
print("Desempaquetado:", p, q, r)


# ------------------------------------------------------------------------------
# 3. EJEMPLOS DE TIPOS DE DATOS (Data Types)
# ------------------------------------------------------------------------------
# Ejemplo 1: Tipos numéricos y texto
texto = "Hola Mundo"          # str
numero = 100                 # int
decimal = 99.9               # float
print("Tipos básicos:", type(texto), type(numero), type(decimal))

# Ejemplo 2: Tipos de datos estructurados (Lista, Tupla, Diccionario)
lista_numeros = [1, 2, 3]    # list
tupla_datos = (10, 20)       # tuple
persona = {"nombre": "Ana"}   # dict
print("Tipos estructurados:", type(lista_numeros), type(tupla_datos), type(persona))

# Ejemplo 3: Tipos Booleanos y Conjuntos
es_valido = True             # bool
conjunto = {1, 2, 3, 3}      # set (elimina duplicados)
print("Booleano y Conjunto:", type(es_valido), conjunto)


# ------------------------------------------------------------------------------
# 4. EJEMPLOS DE OPERADORES ARITMÉTICOS (+, -, *, /, %, **, //)
# ------------------------------------------------------------------------------
# Ejemplo 1: Suma, Resta y Multiplicación
suma = 15 + 5
resta = 20 - 8
multiplicacion = 4 * 3
print("Aritméticos básicos:", suma, resta, multiplicacion)

# Ejemplo 2: División y División Entera
division_normal = 10 / 3    # Resultado flotante
division_entera = 10 // 3   # Resultado entero truncado
print("División normal vs entera:", division_normal, division_entera)

# Ejemplo 3: Módulo (residuo) y Potencia
residuo = 10 % 3            # Residuo de la división
potencia = 2 ** 4           # 2 elevado a la 4
print("Módulo y Potencia:", residuo, potencia)


# ------------------------------------------------------------------------------
# 5. EJEMPLOS DE OPERADORES RELACIONALES / COMPARACIÓN (==, !=, >, <, >=, <=)
# ------------------------------------------------------------------------------
# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
igual = (5 == 5)
diferente = (5 != 3)
print("Igualdad y Desigualdad:", igual, diferente)

# Ejemplo 2: Mayor que (>) y Menor que (<)
es_mayor = (10 > 20)
es_menor = (15 < 30)
print("Mayor y Menor:", es_mayor, es_menor)

# Ejemplo 3: Mayor o igual (>=) y Menor o igual (<=)
mayor_igual = (25 >= 25)
menor_igual = (18 <= 12)
print("Mayor/Igual y Menor/Igual:", mayor_igual, menor_igual)


# ------------------------------------------------------------------------------
# 6. EJEMPLOS DE OPERADORES LÓGICOS (and, or, not)
# ------------------------------------------------------------------------------
# Ejemplo 1: Operador 'and' (Ambas condiciones deben ser verdaderas)
eval_and = (10 > 5) and (5 < 8)
print("Operador AND:", eval_and)

# Ejemplo 2: Operador 'or' (Al menos una condición debe ser verdadera)
eval_or = (10 < 5) or (5 < 8)
print("Operador OR:", eval_or)

# Ejemplo 3: Operador 'not' (Invierte el resultado booleano)
eval_not = not(10 > 5)
print("Operador NOT:", eval_not)
print("programa realizado por marco morquecho NC 1440")