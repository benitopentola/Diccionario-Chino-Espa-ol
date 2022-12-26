import tkinter as tk
import pinyin







# Función para abrir la ventana de ejercicios
def abrir_ejercicios():
  # Crear una nueva ventana y un marco para los botones
  nueva_ventana = tk.Toplevel()
  nueva_ventana.title("Ejercicios")
  marco = tk.Frame(nueva_ventana)
  marco.pack()

  # Crear y empacar 10 botones
  for i in range(10):
    boton = tk.Button(marco, text="Boton {}".format(i + 1))
    boton.pack()

  # Crear el botón "Practicar clasificadores" y asociarlo a la función practicar_clasificadores
  boton_clasificadores = tk.Button(marco, text="Practicar clasificadores", command=practicar_clasificadores)
  boton_clasificadores.pack()

# Crear la ventana principal y los botones
ventana = tk.Tk()
ventana.title("Ventana principal")
boton1 = tk.Button(ventana, text="diccionario")
boton2 = tk.Button(ventana, text="menú")
boton3 = tk.Button(ventana, text="salir")
boton4 = tk.Button(ventana, text="ejercicios", command=abrir_ejercicios)

# Colocar los elementos en la ventana
boton1.pack(side=tk.LEFT)
boton2.pack(side=tk.LEFT)
boton4.pack(side=tk.LEFT)
boton3.pack(side=tk.LEFT)

# Función para practicar los clasificadores
def practicar_clasificadores():
  # Crear una lista de números enteros y utilizar un clasificador para contar cuántos hay en total
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print("Hay {} números en total.".format(len(numeros)))

  # Crear un diccionario con diferentes productos y sus precios, y utilizar un clasificador para contar cuántos productos hay en total
  productos = {
    "manzana": 0.5,
    "pera": 0.75,
    "plátano": 0.25,
    "naranja": 0.65,
    "kiwi": 0.95
  }
  print("Hay {} productos en total.".format(len(productos)))

  # Crear una lista de palabras y utilizar un clasificador para contar cuántas palabras hay en total
  palabras = ["perro", "gato", "ratón", "elefante", "jirafa", "hipopótamo"]
  print("Hay {} palabras en total.".format(len(palabras)))

  # Crear una lista de frases y utilizar un clasificador para contar cuántas frases hay en total
  frases = [
    "El perro ladra.",
    "El gato maulla.",
    "El ratón corre.",
    "El elefante trompetea.",
    "La jirafa tiene el cuello largo."
  ]
  print("Hay {} frases en total.".format(len(frases)))

def abrir_diccionario():
  global cuadro_texto

  nueva_ventana = tk.Toplevel()
  nueva_ventana.title("Diccionario")

  # Crear el cuadro de texto
  cuadro_texto = tk.Entry(nueva_ventana)
  cuadro_texto.pack()

  # Crear el botón para cambiar el texto
  boton_cambiar = tk.Button(nueva_ventana, text="Cambiar texto", command=cambiar_texto)
  boton_cambiar.pack()

def abrir_menú():
  # Crear la ventana de menú
  nueva_ventana = tk.Toplevel()
  nueva_ventana.title("menú")

  # Crear los botones
  boton_opcion1 = tk.Button(nueva_ventana, text="Opcion 1")
  boton_opcion2 = tk.Button(nueva_ventana, text="Opcion 2")
  boton_opcion3 = tk.Button(nueva_ventana, text="Opcion 3")
  boton_opcion4 = tk.Button(nueva_ventana, text="Opcion 4")
  boton_opcion5 = tk.Button(nueva_ventana, text="Opcion 5")
  boton_opcion6 = tk.Button(nueva_ventana, text="Opcion 6")
  boton_opcion7 = tk.Button(nueva_ventana, text="Opcion 7")
  boton_opcion8 = tk.Button(nueva_ventana, text="Opcion 8")
  boton_opcion9 = tk.Button(nueva_ventana, text="Opcion 9")
  boton_opcion10 = tk.Button(nueva_ventana, text="Cambiar fuente")

  # Colocar los botones en la ventana
  boton_opcion1.pack(side=tk.LEFT)
  boton_opcion2.pack(side=tk.LEFT)
  boton_opcion3.pack(side=tk.LEFT)
  boton_opcion4.pack(side=tk.LEFT)
  boton_opcion5.pack(side=tk.LEFT)
  boton_opcion6.pack(side=tk.LEFT)
  boton_opcion7.pack(side=tk.LEFT)
  boton_opcion8.pack(side=tk.LEFT)
  boton_opcion9.pack(side=tk.LEFT)
  boton_opcion10.pack(side=tk.LEFT)


def cerrar_aplicacion():
  ventana.destroy()

def cambiar_texto():
  global cuadro_texto

  # Obtener el texto actual del cuadro de texto
  texto_actual = cuadro_texto.get()

  # Revisar si el texto es chino
  if all(u'\u4e00' <= c <= u'\u9fff' for c in texto_actual):
    # Convertir el texto a pinyin
    pinyin_texto = pinyin.get_pinyin(texto_actual)

    # Eliminar el texto actual
    cuadro_texto.delete(0, tk.END)

    # Insertar el nuevo texto en pinyin
    cuadro_texto.insert(0, pinyin_texto)
  else:
    # Eliminar el texto actual
    cuadro_texto.delete(0, tk.END)

    # Insertar el mensaje de error
    cuadro_texto.insert(0, "IDIOMA INTRODUCIDO NO ES CHINO")

boton1.config(command=abrir_diccionario)
boton2.config(command=abrir_menú)
boton3.config(command=cerrar_aplicacion)

def cambiar_fuente(nueva_fuente):
  global cuadro_texto
  cuadro_texto.config(font=nueva_fuente)
  boton1.config(font=nueva_fuente)
  boton2.config(font=nueva_fuente)
  boton3.config(font=nueva_fuente)
  # ... y así sucesivamente para cada elemento que necesite cambiar la fuente




# Iniciar el bucle de eventos
ventana.mainloop()

