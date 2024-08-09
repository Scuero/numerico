import sympy

x = sympy.symbols('x')

def calcularDerivada():
    unaFuncion = input("Ingrese una funcion cuadratica (usando 'x' como variable): ")
    unaFuncion = sympy.sympify(unaFuncion)
    #Primero la derivo antes del lambdify
    derivadaPunto = sympy.diff(unaFuncion, x)
    unaFuncion = sympy.lambdify(x, unaFuncion, 'numpy')
    evaluarDerivada = sympy.lambdify(x, derivadaPunto, 'numpy')

    return evaluarDerivada(2)


print (calcularDerivada())