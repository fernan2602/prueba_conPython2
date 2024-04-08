calificacion = float(input("Dame la calificaion: \n"))
print("Dame la asistencia: 1 si asistio o 0 no asistio.")
asistencia = int (input())

if ( calificacion > 9.0 and asistencia ==1):
    print("La calificaion es A Exelente con mencion honorifica.")
elif (calificacion > 9.0 and asistencia != 1):
    print("La calificacion es A Exelente")
elif (calificacion > 8.0 and asistencia == 1):
    print ("La calificacion es B muy bine con mencion.")
elif (calificacion > 8.0 and asistencia == 1):
    print("La calificaion es B Muy bien.")
elif (calificacion == 7.5):
    print("La calificacion es C Bien.")
else:
    print("La calificacion es R Reprobado. Lo siento mucho.")     
                