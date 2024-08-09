import numpy as np
import matplotlib.pyplot as plt

ALPHA = 150000
BETA = 0.0192
GRAVEDAD = 3.72
MASA = 1000
ALTURA_INICIAL = 130000
VELOCIDAD_INICIAL = -5555
PASO = 0.01
EULER = np.e
HAP = 13000
CONDICION_INICIAL = np.array([ALTURA_INICIAL, VELOCIDAD_INICIAL])

def evaluar_f_en(condicion):
    return (np.array( [condicion[1], (GRAVEDAD*-1)+((1/MASA)*BETA*(pow(EULER, -1*condicion[0]/ALPHA))*pow(condicion[1],2))]))

def calcular_quno(condicion):
    return evaluar_f_en(condicion)*PASO

def calcular_qdos(condicionInicial, qUno):
    return evaluar_f_en(condicionInicial+qUno)*PASO

def calcular_siguiente(condicionInicial):
    qUno = calcular_quno(condicionInicial)
    qDos = calcular_qdos(condicionInicial, qUno)
    return condicionInicial+((1/2)*(qUno+qDos))

def calcular(alturas, velocidades, tiempo):
    condicionInicial = CONDICION_INICIAL
    contador = 0
    while (condicionInicial[0] > HAP):
        tiempo.append(contador*PASO)
        alturas.append(condicionInicial[0])
        velocidades.append(condicionInicial[1])
        condicionInicial = calcular_siguiente(condicionInicial)
        contador += 1

def graficar(alturas, velocidades, tiempo):
    plt.figure()
    plt.plot(tiempo, alturas, linestyle='-', color='blue', linewidth=0.6)
    plt.plot(tiempo, velocidades, linestyle='-', color='red', linewidth=0.7)
    plt.xlabel('Tiempo')
    plt.title('Altura y velocidad en funcion del tiempo')
    plt.grid(True, color='gray', linestyle='-', linewidth=0.3, alpha=0.3)
    plt.xlim(0, 42)
    plt.ylim(-5555, 130000)
    plt.xticks(np.arange(0, 42, 1))
    plt.yticks(np.arange(-5555, 130000, 4000))
    plt.legend(labels=['Altura (Azul)', 'Velocidad (Rojo)'], loc='upper right')
    plt.subplots_adjust(left=0.04, right=0.98, top=0.95, bottom=0.06)
    plt.show()

alturas = []
velocidades = []
tiempo = []
calcular(alturas, velocidades, tiempo)
graficar(alturas, velocidades, tiempo)