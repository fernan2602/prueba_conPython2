
#INICIO
print("Dame saldo actual")
saldo = float(input())

#empieza la condicion 

if (saldo <10000.00):
    saldo = saldo * (1 + 0.03)
else:
    saldo = saldo * (1 + 0.04)
20
#fin del if

print("Saldo final es" + str(saldo))

 #FIN


 
