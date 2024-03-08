from decimal import Decimal, getcontext, ROUND_DOWN

def falsa_posicion(f, xl, xu, cifras_significativas, max_iter):
    """
    Encuentra una solución aproximada de la ecuación f(x) = 0 utilizando el método de la falsa posición.

    :param f: Función f(x).
    :param xl: Extremo izquierdo del intervalo inicial.
    :param xu: Extremo derecho del intervalo inicial.
    :param cifras_significativas: Cantidad de cifras significativas para el error esperado.
    :param max_iter: Número máximo de iteraciones permitidas.
    :return: Aproximación de la solución, el número de iteraciones realizadas y los errores de aproximación.
    """
    # Configura la precisión de Decimal
    getcontext().prec = cifras_significativas + 10  # Se agrega margen para evitar errores de redondeo, esto nos revelara mayor o menor cantidad de decimales

    iteraciones = 0
    errores_aproximacion = []

    while iteraciones < max_iter:
        # Calcula los valores de la función en los extremos del intervalo
        fxl = f(xl)
        fxu = f(xu)

        # Verifica si la solución ya fue encontrada
        if fxl == 0:
            return xl, iteraciones + 1, [0.0]
        elif fxu == 0:
            return xu, iteraciones + 1, [0.0]

        # Calcula la nueva aproximación usando la fórmula dada
        x_aprox = xu - (fxu * (xl - xu)) / (fxl - fxu)

        # Calcula el valor de la función en la nueva aproximación
        fx_aprox = f(x_aprox)

        # Calcula el error de aproximación
        if iteraciones > 0:
            error_aproximacion = abs((x_aprox - x_aprox_anterior) / x_aprox) * 100
        else:
            error_aproximacion = float('inf')

        # Agrega el error de aproximación a la lista
        errores_aproximacion.append(error_aproximacion)

        # Se anexa el cálculo para el error esperado
        error_esperado = 0.5 * 10**(2 - cifras_significativas)

        # Comprueba la convergencia con el error esperado
        if error_aproximacion < error_esperado:
            resultado_truncado = Decimal(str(x_aprox)).quantize(Decimal('1e-{0}'.format(cifras_significativas)), rounding=ROUND_DOWN)
            return float(x_aprox), iteraciones + 1, [float(error) for error in errores_aproximacion], float(resultado_truncado)

        # Actualiza los extremos del intervalo
        if fx_aprox * fxl < 0:
            xu = x_aprox
        else:
            xl = x_aprox

        # Actualiza la aproximación anterior
        x_aprox_anterior = x_aprox

        # Muestra el valor de la solución aproximada en cada iteración
        print("Iteración {}: Solución Aproximada = {}, Error de Aproximación = {}%".format(iteraciones + 1, float(x_aprox), error_aproximacion))

        iteraciones += 1

    # En caso de no convergencia
    raise Exception("El método de falsa posición no converge después de {} iteraciones.".format(max_iter))


# Ejemplo de uso:
if __name__ == "__main__":
    # Define la función f(x)
    def f(x):
        return x**2 - 2

    # Solicita al usuario los extremos del intervalo
    xl = float(input("Ingrese el extremo izquierdo del intervalo (xl): "))
    xu = float(input("Ingrese el extremo derecho del intervalo (xu): "))
    
    # Solicita la cantidad de cifras significativas al usuario
    cifras_significativas = int(input("Ingrese la cantidad de cifras significativas: "))
    
    # Número máximo de iteraciones
    max_iter = 1000

    # Llama al método de falsa posición
    try:
        resultado, num_iteraciones, errores_aproximacion, resultado_truncado = falsa_posicion(f, xl, xu, cifras_significativas, max_iter)

        # Muestra los resultados finales
        print("\nSolución aproximada:", resultado)
        print("Solución truncada:", resultado_truncado)
        print("Número de iteraciones:", num_iteraciones)

        # Muestra los errores de aproximación para cada iteración
        print("\nErrores de Aproximación:")
        for i, error in enumerate(errores_aproximacion):
            print("Iteración {}: {}%".format(i + 1, error))

    except Exception as e:
        print("\nError:", e)
