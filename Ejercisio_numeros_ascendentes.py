numero = 0
numeros = []
resultado = 'False'
numero_mayor = 0
for i in range (3):
    numero = int (input("Ingrese numero: "))
    
    while  (resultado == 'False' ) :
        if (numero>numero_mayor):
            numero_mayor = numero
            numeros.append(numero_mayor)
            print(numero_mayor)
        if (numero<numero_mayor):
            numero_mayor = numero
            numeros.append(numero_mayor)
            print(numero_mayor)
        else:
            resultado = 'True'
            break
    resultado = 'False'
print (numeros)
