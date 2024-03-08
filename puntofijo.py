from decimal import Decimal, getcontext, ROUND_DOWN

def punto_fijo(g, x0, cifras_significativas, max_iter):
    """
    Encuentra una solución aproximada de la ecuación g(x) = x utilizando el método de punto fijo.

    :param g: Función de iteración g(x).
    :param x0: Valor inicial.
    :param cifras_significativas: Cantidad de cifras significativas para el error esperado.
    :param max_iter: Número máximo de iteraciones permitidas.
    :return: Aproximación de la solución, el número de iteraciones realizadas y los errores de aproximación.
    """
    # Configura la precisión de Decimal
    getcontext().prec = cifras_significativas + 10  # Se agrega margen para evitar errores de redondeo

    # Calcular el error esperado a partir de las cifras significativas
    error_esperado = Decimal(0.5) * Decimal(10)**Decimal(2 - cifras_significativas)

    iteraciones = 0
    x = Decimal(str(x0))
    errores_aproximacion = []

    while iteraciones < max_iter:
        x_anterior = x
        x = g(x)

        # Calcula el error de aproximación
        error_aproximacion = abs(((x - x_anterior) / x )*100)

        # Agrega el error de aproximación a la lista
        errores_aproximacion.append(error_aproximacion)

        # Comprueba la convergencia con el error esperado
        if error_aproximacion < error_esperado:
            # Trunca el resultado al número deseado de cifras significativas
            resultado_truncado = x.quantize(Decimal('1e-{0}'.format(cifras_significativas)), rounding=ROUND_DOWN)
            return float(x), float(resultado_truncado), iteraciones + 1, [float(error) for error in errores_aproximacion]

        # Muestra el resultado del error de aproximación para cada iteración
        print("Iteración {}: Aproximación = {}, Error de Aproximación = {}%".format(iteraciones+1 , float(x), float(error_aproximacion)))

        iteraciones += 1

    # En caso de no convergencia
    raise Exception("El método de punto fijo no converge después de {} iteraciones.".format(max_iter))


# Ejemplo de uso:
if __name__ == "__main__":
    # Define la función de iteración g(x)
    def g(x):
        return x**2 - 2

    # Solicita al usuario el valor inicial
    x0 = Decimal(input("Ingrese el valor inicial x0: "))
    
    # Solicita la cantidad de cifras significativas al usuario
    cifras_significativas = int(input("Ingrese la cantidad de cifras significativas: "))
    
    # Número máximo de iteraciones
    max_iter = 1000

    # Llama al método de punto fijo
    try:
        resultado, resultado_truncado, num_iteraciones, errores_aproximacion = punto_fijo(g, x0, cifras_significativas, max_iter)

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
