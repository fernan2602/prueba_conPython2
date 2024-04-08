
nota_para_aprobar = 3
cantidad_notas = 3 
respuesta = "s"
total_alumnos = 0
total_suspendidas = 0
total_aprobadas = 0
total_alumnos_todo_aprobado = 0
total_alumnos_alguna_suspendida = 0
suma_notas_medias_repetidores = 0
suma_notas_medias_no_repetidores = 0
alumno_nota_media_mas_alta = ""
nota_media_mas_alta = 0
total_repetidores = 0
total_no_repetidores = 0
def new_func(nota_media):
    if nota_media < 7.5:
        valor_equivalente = "Reprobado"
    elif nota_media < 8:
        valor_equivalente = "bien "
    elif nota_media < 9:
        valor_equivalente = "Muy Bien"
    elif nota_media < 10:
        valor_equivalente = "Excelente"
    else:
        valor_equivalente = "Sobresaliente"
    return valor_equivalente

while respuesta.lower() == "s":
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    repetidor = input("Repetidor: [s/n] ")
    nota_maxima = 0
    nota_minima = 11
    suma_notas = 0
    suspendidas = 0
    aprobadas = 0
    nota = -1
    for i in range(cantidad_notas):
        while nota <    0 or nota > 10:
            nota = float(input("Ingrese la nota #" + str(i+1) + ": "))
        suma_notas += nota
        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota

        if nota < nota_para_aprobar:
            suspendidas += 1
            total_suspendidas += 1
        else:
            aprobadas += 1
            total_aprobadas += 1
        nota = -1
    total_alumnos += 1
    nota_media = suma_notas / cantidad_notas
    if nota_media > nota_media_mas_alta:
        alumno_nota_media_mas_alta = nombre
        nota_media_mas_alta = nota_media
    if suspendidas <= 0:
        total_alumnos_todo_aprobado += 1
    else:
        total_alumnos_alguna_suspendida += 1
    if repetidor.lower() == "s":
        suma_notas_medias_repetidores += nota_media
        total_repetidores += 1
    else:
        suma_notas_medias_no_repetidores += nota_media
        total_no_repetidores += 1
    print("Estadística de " + nombre)
    if repetidor.lower() == "s":
        print("-Repetidor: sí")
    else:
        print("-Repetidor: no")
    print("-Nota máxima: " + str(nota_maxima))
    print("-Nota mínima: " + str(nota_minima))
    valor_equivalente = ""
    valor_equivalente = new_func(nota_media)

    print("-Nota media: " + str(nota_media) + " ("+valor_equivalente+")")
    print("-Cuántas suspendidas: " + str(suspendidas))
    print("-Cuántas aprobadas: " + str(aprobadas))
    respuesta = input("Se van a introducir más alumnos? [s/n] ")


nota_media_repetidores = 0.0
if total_repetidores > 0:
    nota_media_repetidores = suma_notas_medias_repetidores / total_repetidores
nota_media_no_repetidores = 0.0
if total_no_repetidores > 0:
    nota_media_no_repetidores = suma_notas_medias_no_repetidores / total_no_repetidores
print("Estadística de la clase")
print("-Cuántos alumnos: " + str(total_alumnos))
print("-Cuántas notas suspendidas: " + str(total_suspendidas))
print("-Cuántas notas aprobadas: " + str(total_aprobadas))
print("-Cuántos alumnos con todo aprobado: " + str(total_alumnos_todo_aprobado))
print("-Cuántos alumnos con alguna suspendida: " +
      str(total_alumnos_alguna_suspendida))
print("-Nota media de los repetidores: " + str(nota_media_repetidores))
print("-Nota media de los no repetidores: " + str(nota_media_no_repetidores))
print("-Alumno con la nota media más alta: " +
      str(alumno_nota_media_mas_alta) + " (" + str(nota_media_mas_alta) + ")")