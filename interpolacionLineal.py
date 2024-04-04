def interpolacion_lineal(x0, y0, x1, y1, xi):
  """
  Calcula el valor interpolado de y para un valor de x dado utilizando interpolación lineal.

  Args:
    x0: Valor de x del primer punto de datos.
    y0: Valor de y del primer punto de datos.
    x1: Valor de x del segundo punto de datos.
    y1: Valor de y del segundo punto de datos.
    xi: Valor de x para el que se interpola.

  Returns:
    Valor interpolado de y para xi.
  """
  if xi < x0 or xi > x1:
    raise ValueError(f"El valor de xi ({xi}) debe estar dentro del intervalo [x0, x1]")

  yi = y0 + ((xi - x0) * (y1 - y0)) / (x1 - x0)
  return yi

# Ejemplo de uso
x0 = 0
y0 = 1
x1 = 2
y1 = 5
xi = 1.5

yi_interpolado = interpolacion_lineal(x0, y0, x1, y1, xi)
print(f"Valor interpolado para x = {xi}: {yi_interpolado}")
