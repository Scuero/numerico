import sympy

x = sympy.symbols('x')
TOLERANCIA = 10**(-9)

def newton_raphson(funcion, funcionDerivada, unPunto):
    raiz = unPunto-(funcion(unPunto)/funcionDerivada(unPunto))
    if ( abs(funcion(raiz)) < TOLERANCIA ):
        return round(raiz, 4)
    
    return newton_raphson( funcion, funcionDerivada, raiz )

def encontrarRaiz():
    unaFuncion = input("Ingrese una funcion cuadratica (usando 'x' como variable): ")
    unaFuncion = sympy.sympify(unaFuncion)
    funcionDerivada = sympy.diff(unaFuncion, x)
    
    unaFuncion = sympy.lambdify(x, unaFuncion, 'numpy')
    funcionDerivada = sympy.lambdify(x, funcionDerivada, 'numpy')

    puntoInicial = input("Ingrese un punto inicial(en lo posible cercano a la raiz de la funcion) ")
    puntoInicial = float(puntoInicial)

    print( newton_raphson(unaFuncion, funcionDerivada, puntoInicial) )

encontrarRaiz()