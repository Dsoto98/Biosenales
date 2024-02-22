import numpy as np
import matplotlib.pyplot as plt
import math
# a) Definición de los vectores
a = [67.1, 1, -0.3, 5.2, -6]
b = [1, 3, 2.2, 5.1, 1]

# b) Multiplicación escalar de a . b
def scalar_multiplication(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        return "Los vectores deben tener la misma longitud para la multiplicación escalar."
    result = sum(x * y for x, y in zip(vector_a, vector_b))
    return result

# c) Multiplicación punto a punto de a . b
def multiplication(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        return "Los vectores deben tener la misma longitud para la multiplicación punto a punto."
    result = [x * y for x, y in zip(vector_a, vector_b)]
    return result

print("Multiplicación escalar de a.b:", scalar_multiplication(a, b))
print("Multiplicación punto a punto de a.b:", multiplication(a, b))
# d) Contruccion de la matriz
A = np.array([[2, -1, -3],[4, -1.5, -2.5],[7.3, -0.9, -0.2]])
# print("Matriz A:") Lo descomento si quiero ver la matriz A en consola
# print(A)

#e) Obtencion de su la transpuesta de a
A_transpuesta = np.transpose(A)
print("Transpuesta de A:")
print(A_transpuesta)
#g) Acceder al valor de la primera fila, tecera colimna 
valor = A[0, 2]
print("Valor en la primera fila, tercera columna de la matriz A:", valor)
#h) Obtenga la segunda fila de ddicha matriz. imprimalo en consola.
segunda_fila = A[1, :]
print("Segunda fila de la matriz A:", segunda_fila)
#i) Consulte  el  comando  para  conocer  las  dimensiones  de  una  matriz,  utilícelo  con  la  matriz  A e imprímalo en consola.

dimensiones_A = A.shape
print("Dimensiones de la matriz A:", dimensiones_A)

# J,K,L,M, N
# Definir las funciones y[n] y y2[n]
def y(n):
    return math.sin(math.pi * 0.18 * n)

def y2(n):
    return math.cos(2 * math.pi * 0.03 * n)

# Generar valores para y[n] y y2[n] en el intervalo 0 <= n <= 80
valores_y = [y(n) for n in range(81)]
valores_y2 = [y2(n) for n in range(81)]

# Generar la tercera señal s[n] = y[n] + y2[n]
tercera_senal = [valores_y[i] + valores_y2[i] for i in range(len(valores_y))]

# Generar la cuarta señal t[n] = y[n] * y2[n]
cuarta_senal = [valores_y[i] * valores_y2[i] for i in range(len(valores_y))]

# Graficar y[n] y y2[n] en la misma figura
plt.figure(figsize=(10, 5))
plt.plot(valores_y, label='y[n] = sin(π * 0.18 * n)')
plt.plot(valores_y2, label='y2[n] = cos(2π * 0.03 * n)')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.title('Señales y[n] y y2[n]')
plt.legend()
plt.grid(True)
plt.show()

# Graficar s[n] y t[n] en la misma figura
plt.figure(figsize=(10, 5))
plt.plot(tercera_senal, label='s[n] = y[n] + y2[n]')
plt.plot(cuarta_senal, label='t[n] = y[n] * y2[n]')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.title('Señales s[n] y t[n]')
plt.legend()
plt.grid(True)
plt.show()

