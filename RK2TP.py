import numpy as np
import matplotlib.pyplot as plt

ALPHA = 150000
BETA = 0.0192
ETA = 0.3600
GRAVEDAD = 3.72
MASA = 1000
ALTURA_INICIAL = 130000
VELOCIDAD_INICIAL = -5555
ALTURA_ETAPA_2 = 13000
VELOCIDAD_ETAPA_2 = -1417.67
ALTURA_ETAPA_3 = 2000
ALTURA_FINAL_ETAPA_3 = 20
PASO = 0.01
K1 = 25
K2 = 30
VELOCIDAD_ESCAPE_CAUDAL = 1000
EULER = np.e
CONDICION_INICIAL = np.array([ALTURA_INICIAL, VELOCIDAD_INICIAL])
CONDICION_ETAPA_2 = np.array([ALTURA_ETAPA_2, VELOCIDAD_ETAPA_2])

def evaluar_etapa1(condicion):
    return (np.array([condicion[1], (GRAVEDAD * -1) + ((1 / MASA) * BETA * (pow (EULER, -1 * condicion[0] / ALPHA)) * pow(condicion[1], 2))]))

def evaluar_etapa2(condicion):
    return (np.array([condicion[1] ,(GRAVEDAD * -1) + (ETA/MASA) * pow(condicion[1], 2)]))

def evaluar_etapa3(condicion):
    caudal = ((MASA * GRAVEDAD / VELOCIDAD_ESCAPE_CAUDAL) - K1 * (condicion[0] - ALTURA_FINAL_ETAPA_3) - K2 * condicion[1])
    if caudal < 0:
        caudal = 0
    return np.array([condicion[1], (GRAVEDAD * -1) + (MASA ** -1) * (caudal * (VELOCIDAD_ESCAPE_CAUDAL - condicion[1]))])

def calcular_quno(condicion, etapa):
    return etapa(condicion) * PASO

def calcular_qdos(condicionInicial, qUno, etapa):
    return etapa(condicionInicial + qUno) * PASO

def calcular_siguiente(condicionInicial, etapa):
    qUno = calcular_quno(condicionInicial, etapa)
    qDos = calcular_qdos(condicionInicial, qUno, etapa)
    return condicionInicial + ((1/2) * (qUno + qDos))

def calcular(condicion, etapa, altura_limite, t_inicial = 0, etapa_3 = False):
    alturas = []
    velocidades = []
    tiempo = []
    caudal = []
    condicionInicial = condicion
    contador = 0

    while (int(condicionInicial[0]) > altura_limite):
        tiempo.append(contador * PASO + int(t_inicial))
        alturas.append(condicionInicial[0])
        velocidades.append(condicionInicial[1])
        condicionInicial = calcular_siguiente(condicionInicial, etapa)
        if etapa_3:
            caudal_act = ((MASA * GRAVEDAD / VELOCIDAD_ESCAPE_CAUDAL) - K1 * (alturas[-1] - ALTURA_FINAL_ETAPA_3) - K2 * velocidades[-1])
            if caudal_act < 0:
                caudal.append(0)
            else:
                caudal.append(caudal_act)
        contador += 1
    graficar_posicion(alturas, tiempo)
    graficar_velocidad(velocidades, tiempo)
    if etapa_3:
        graficar_caudal(caudal, tiempo)
    return alturas[-1], velocidades[-1], tiempo[-1]

def graficar_posicion(alturas, tiempo):
    plt.figure()
    plt.plot(tiempo, alturas, linestyle = '-', color = 'blue', linewidth = 1)
    plt.xlabel('Tiempo')
    plt.title('Altura en funcion del tiempo')
    plt.grid(True, color = 'gray', linestyle = '-', linewidth = 0.3, alpha = 0.3)
    plt.xlim(tiempo[0], tiempo[-1])
    plt.ylim(alturas[-1], alturas[0])
    plt.xticks(np.arange(tiempo[0], tiempo[-1], 1))
    plt.yticks(np.arange(alturas[-1], alturas[0], abs(alturas[-1] - alturas[0]) // int(tiempo[-1] - tiempo[0])))
    plt.legend(labels=['Altura (Azul)'], loc = 'upper right')
    plt.subplots_adjust(left = 0.10, right = 0.98, top = 0.95, bottom = 0.06)
    plt.show()

def graficar_velocidad(velocidades, tiempo):
    plt.figure()
    plt.plot(tiempo, velocidades, linestyle = '-', color = 'red', linewidth = 1)
    plt.xlabel('Tiempo')
    plt.title('Velocidad en funcion del tiempo')
    plt.grid(True, color = 'gray', linestyle = '-', linewidth = 0.3, alpha = 0.3)
    plt.xlim(tiempo[0], tiempo[-1])
    v_min = min(velocidades)
    plt.ylim(v_min, 0)
    plt.xticks(np.arange(tiempo[0], tiempo[-1], 1))
    plt.yticks(np.arange(int(v_min), 0, int(abs(v_min) // int(tiempo[-1] - tiempo[0]))))
    plt.legend(labels = ['Velocidad (Rojo)'], loc = 'upper right')
    plt.subplots_adjust(left = 0.10, right = 0.98, top = 0.95, bottom = 0.06)
    plt.show()

def graficar_caudal(caudal, tiempo):
    plt.figure()
    plt.plot(tiempo, caudal, linestyle = '-', color = 'green', linewidth = 1)
    plt.xlabel('Tiempo')
    plt.title('Caudal en funcion del tiempo')
    plt.grid(True, color = 'gray', linestyle = '-', linewidth = 0.3, alpha = 0.3)
    plt.xlim(tiempo[0], tiempo[-1])
    max_caudal = max(caudal)
    plt.ylim(0, max_caudal)
    plt.xticks(np.arange(tiempo[0], tiempo[-1], 1))
    plt.yticks(np.arange(0, max_caudal, max_caudal / int(tiempo[-1] - tiempo[0])))
    plt.legend(labels = ['Caudal (Verde)'], loc = 'upper right')
    plt.subplots_adjust(left = 0.10, right = 0.98, top = 0.95, bottom = 0.06)
    plt.show()

    

a_final, v_final, t_final = calcular(CONDICION_INICIAL, evaluar_etapa1, ALTURA_ETAPA_2)
print('etapa 1')
print(a_final, v_final, t_final)
a_final, v_final, t_final = calcular(np.array([a_final, v_final]), evaluar_etapa2, ALTURA_ETAPA_3, t_final)
print('etapa 2')
print(a_final, v_final, t_final)
a_final, v_final, t_final = calcular(np.array([a_final, v_final]), evaluar_etapa3, ALTURA_FINAL_ETAPA_3, t_final, True)
print('etapa 3')
print(a_final, v_final, t_final)