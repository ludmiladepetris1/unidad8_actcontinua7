# EJERCICIO 1: En una carrera participaron varios corredores.
# Ordenar los tiempos de menor a mayor utilizando Insertion Sort.

# ----------------------------------------------------------------------

# -- SUS TIEMPOS (EN MINUROS) FUERON:
tiemposMin=[43,32,40,55,30,28]
print("Tiempos sin ordenar:",tiemposMin)

# ----------------------------------------------------------------------

# -- RECORREMOS
# Recorremos la lista de ventas por semana:

for i in range(1,len(tiemposMin)):
    valor= tiemposMin[i] # Guarda el elemento actual; el nro que quieremos acomodar en el lugar correcto.
    j= i - 1 # Hace que j apunte al elemento de la izquierda.

    #"Mientras haya elementos a la izquierda y sean más grandes que el valor, seguí moviéndolos."
    while j >= 0 and tiemposMin[j] > valor:
        tiemposMin[j+1] = tiemposMin[j] # Copiá el número grande una posición hacia la derecha.
        j= j-1 # mirá el número que está más a la izquierda.

        # Cuando no hay mas numeros mas grande que el numero guardado en "valor"
        # Coloca ese numero en el casillero que quedo libre.
        tiemposMin[j+1] = valor

print("Tiempos ordenados:",tiemposMin)


               