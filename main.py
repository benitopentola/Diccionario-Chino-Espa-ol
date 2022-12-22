import tkinter as tk
import pinyin

# Declarar la variable global cuadro_texto
cuadro_texto = None

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("DICCIONARIO CHINO ESPAÑOL")

# Crear el título en letras grandes
titulo = tk.Label(ventana, text="DICCIONARIO CHINO ESPAÑOL", font=("Helvetica", 16))
titulo.pack()

# Crear los botones
boton1 = tk.Button(ventana, text="diccionario")
boton2 = tk.Button(ventana, text="menú")
boton3 = tk.Button(ventana, text="salir")

# Colocar los elementos en la ventana
boton1.pack(side=tk.LEFT)
boton2.pack(side=tk.LEFT)
boton3.pack(side=tk.LEFT)

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

# Iniciar el bucle de eventos
ventana.mainloop()

