import tkinter as tk
import random

# Función para mostrar el resultado del ejercicio
def mostrar_resultado(resultado):
  # Crear una nueva ventana y asignarle un título
  ventana = tk.Tk()
  ventana.title("Resultado")

  # Mostrar el resultado en una etiqueta
  etiqueta = tk.Label(ventana, text=resultado)
  etiqueta.pack()

# Lista de clasificadores en chino mandarín
clasificadores = ["个", "条", "张", "只", "棵"]

# Lista de palabras a clasificar
palabras = ["电脑", "椅子", "手机", "苹果", "树"]

# Número de ejercicios a realizar
num_ejercicios = 5

# Realizar los ejercicios
for i in range(num_ejercicios):
  # Seleccionar una palabra y un clasificador al azar
  palabra = random.choice(palabras)
  clasificador = random.choice(clasificadores)

  # Pedir al usuario que escriba el número correcto de objetos de la palabra seleccionada usando el clasificador seleccionado
  num = int(input("¿Cuántos {} de {} hay? ".format(clasificador, palabra)))

  # Comprobar si la respuesta del usuario es correcta
  if num == 1:
    resultado = "¡Correcto!"
  else:
    resultado = "Incorrecto. La respuesta correcta es 1."

  # Mostrar el resultado en una ventana GUI
  mostrar_resultado(resultado)
