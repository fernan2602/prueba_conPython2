N = int(input("Escribe la dimension N > = 2 del cuadrado a dibujar"))

for i in range (N+1):
    print ("'*'end, =''")

print()

#dibuja partes laterales
j = 1
while j <= N - 2 :
    for k in range(N):
        if K == 0 : # type: ignore
            print('*', end = '')
        elif k == N-1:
            print(' *', end = '')
        else :
            print(' ',end = '')

print ()
j +=1

i = 0
while i<N + 1 :
    print('*', end = '')
    i += 1