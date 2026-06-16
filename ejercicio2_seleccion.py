# Ejercicio 2: Ordenamiento por Selección (Selection Sort) Una biblioteca registró la cantidad de libros prestados por día durante una semana.
# Se desea ordenar las cantidades de menor a mayor utilizando el método Selection Sort.

# ------------------------------------------------------------------------------------------------

librosPrestados= [12,9,11,18,2,10]
print("Lista de libros prestados por semana sin ordenar:",librosPrestados)

# Se le pone -1 porque en Selection Sort no hace falta recorrer la última posición.
# Porque cuando llegás a la última posición (índice 5) ya no queda ningún elemento a la derecha para comparar.

for i in range(0,len(librosPrestados)-1):
    # Al comenzar cada vuelta, suponemos que el menor número está en la posición actual.
    menor= i
    # Busca en el resto de la lista si existe un número más pequeño.
    for j in range (i+1,len(librosPrestados)):
        # Pregunta: "¿El número que estoy mirando es menor que el mínimo encontrado hasta ahora?"
        if librosPrestados[j] < librosPrestados[menor]:
            # # Si es true cambia el menor, sino sigue igual
            menor= j

    # -- INTERCAMBIO 
    aux= librosPrestados[i] # Guardamos el valor de la posición actual.
    librosPrestados[i] = librosPrestados[menor] # Ponemos el mínimo en la posición correcta.
    librosPrestados[menor] = aux # Recuperamos el valor que guardamos en la varible aux.

print("Lista de libros prestados por semana ordenados:",librosPrestados)
