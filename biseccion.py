import sympy

x = sympy.symbols('x')
TOLERANCIA = 10**(-6)

def biseccionar(unaFuncion, a, b):
    izquierdo = a
    derecho = b
    medio = (izquierdo + derecho)/2
    fMedio = evaluarFuncion(unaFuncion, medio)
    fIzquierdo = evaluarFuncion(unaFuncion, izquierdo)
    if ( abs(fMedio) < TOLERANCIA ):
        return round(medio, 5)
    # SI f(izquierdo) y f(medio) son del mismo signo, => ambos estan en el mismo cuadrante => el punto medio es el nuevo extremo izquierdo
    if ( fMedio * fIzquierdo > 0 ):
        return biseccionar(unaFuncion, medio, derecho)
    return biseccionar(unaFuncion, izquierdo, medio)


def evaluarFuncion(unaFuncion, unPunto):
    return unaFuncion(unPunto) 

def encontrarRaiz():
    unaFuncion = input("Ingrese una funcion (usando 'x' como variable): ")
    unaFuncion = sympy.sympify(unaFuncion)
    unaFuncion = sympy.lambdify(x, unaFuncion, 'numpy')

    izquierdo = input("Ingrese el extremo izquierdo del intervalo que contiene a la raiz ")
    derecho = input("Ingrese el extremo derecho del intervalo que contiene a la raiz ")
    izquierdo = float(izquierdo)
    derecho = float(derecho)

    print( biseccionar(unaFuncion, izquierdo, derecho) )

encontrarRaiz()