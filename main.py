import tkinter as tk

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
  nueva_ventana = tk.Toplevel()
  nueva_ventana.title("Diccionario")

def abrir_menú():
  nueva_ventana = tk.Toplevel()
  nueva_ventana.title("menú")

def cerrar_aplicacion():
  ventana.destroy()

boton1.config(command=abrir_diccionario)
boton2.config(command=abrir_menú)
boton3.config(command=cerrar_aplicacion)

# Iniciar el bucle de eventos
ventana.mainloop()
d

