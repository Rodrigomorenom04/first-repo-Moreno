# Autor: Rodrigo Moreno...

clases = []   
notas = []    

print("Registro de notas")
print("Escribe -1 en la nota cuando quieras terminar.")
print()

while True:
    # 1) Pedir el nombre de la clase
    nombre_clase = input("Nombre de la clase: ")

    # 2) Pedir la nota, y repetir si no es valida
    while True:
        entrada = input("Nota (0 a 100, o -1 para terminar): ")

        # Convertir el texto a numero
        nota = int(entrada)

        # -1 significa terminar el programa
        if nota == -1:
            break

        # Validar que este dentro del rango permitido
        if nota < 0 or nota > 100:
            print("Aviso: la nota debe estar entre 0 y 100. Intenta de nuevo.")
        else:
            # Nota valida: la guardamos junto con su clase
            clases.append(nombre_clase)
            notas.append(nota)
            break

    # Si la nota fue -1, salimos del bucle principal
    if nota == -1:
        break

# ----- Resultados finales -----
print()
print("----- Resultado final -----")

if len(notas) == 0:
    print("No se ingreso ninguna nota.")
else:
    # Mostrar todas las notas ingresadas
    print("Notas ingresadas:")
    for i in range(len(notas)):
        print("  " + clases[i] + ": " + str(notas[i]))

    # Cantidad de notas validas
    print("Cantidad de notas validas: " + str(len(notas)))

    # Calcular el promedio sumando todas las notas
    suma = 0
    for n in notas:
        suma = suma + n

    promedio = suma / len(notas)
    print("Promedio: " + str(promedio))