# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AMRvFIb4out4p4vC7IYXI2gv8Rz2T9qT
"""

# Definir una lista vacía para almacenar los datos de los ejemplares
ejemplares = []
# Definir una función para registrar la adquisición de un ejemplar
def registrar_ejemplar():
    titulo = input("Ingrese el título del ejemplar: ")
    autor = input("Ingrese el autor del ejemplar: ")
    editorial = input("Ingrese la editorial del ejemplar: ")
    ejemplar = {"titulo": titulo, "autor": autor, "editorial": editorial}
    ejemplares.append(ejemplar)
    print("El ejemplar ha sido registrado exitosamente.")
# Definir una función para mostrar los datos de los ejemplares en pantalla
def mostrar_ejemplares():
    for ejemplar in ejemplares:
        print(f"Título: {ejemplar['titulo']}\nAutor: {ejemplar['autor']}\nEditorial: {ejemplar['editorial']}\n")
# Definir una función para buscar un ejemplar por título
def buscar_ejemplar():
    titulo = input("Ingrese el título del ejemplar a buscar: ")
    encontrado = False
    for ejemplar in ejemplares:
        if ejemplar["titulo"].lower() == titulo.lower():
            print(f"Título: {ejemplar['titulo']}\nAutor: {ejemplar['autor']}\nEditorial: {ejemplar['editorial']}\n")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún ejemplar con ese título.")
# Definir una función para generar un reporte tabular de todos los ejemplares existentes
def generar_reporte():
    print("Reporte de ejemplares:")
    print("Título\tAutor\tEditorial")
    for ejemplar in ejemplares:
        print(f"{ejemplar['titulo']}\t{ejemplar['autor']}\t{ejemplar['editorial']}")
# Definir una función principal para mostrar el menú de opciones
def main():
    opcion = ""
    while opcion != "5":
        print("Menú de Biblioteca")
        print("1. Registrar la adquisición de un ejemplar")
        print("2. Consultas en pantalla")
        print("3. Consultar los datos de un título")
        print("4. Reporte tabular de todos los ejemplares existentes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_ejemplar()
        elif opcion == "2":
            mostrar_ejemplares()
        elif opcion == "3":
            buscar_ejemplar()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Gracias por utilizar nuestro sistema.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
# Ejecutar la función principal
if __name__ == "__main__":
    main()