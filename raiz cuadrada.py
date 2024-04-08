def raiz_cuadrada(numero):
    # Asumimos una aproximación inicial
    aproximacion = numero / 2
    # Definimos la precisión deseada
    precision = 0.0001

    # Usamos un bucle para mejorar la aproximación
    while True:
        # Calculamos una nueva aproximación usando el método de Newton
        nueva_aproximacion = (aproximacion + numero / aproximacion) / 2
        # Si la diferencia entre la nueva aproximación y la anterior es menor que la precisión deseada, salimos del bucle
        if abs(nueva_aproximacion - aproximacion) < precision:
            break
        # Actualizamos la aproximación
        aproximacion = nueva_aproximacion

    return nueva_aproximacion

# Prueba de la función
numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada(numero))








