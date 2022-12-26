import tkinter as tk
import pinyin
import cmd

# Clase para la consola de clasificadores
class ClasificadoresConsola(cmd.Cmd):
  # Método para manejar el comando "salir"
  def do_salir(self, args):
    print("Saliendo de la consola de clasificadores...")
    return True

  # Método para manejar cualquier otro comando
  def default(self, line):
    print("Comando no reconocido: {}".format(line))

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

#Función para practicar los clasificadores
def practicar_clasificadores():
  consola = ClasificadoresConsola()
  consola.cmdloop()


#Iniciar la ventana principal
ventana.mainloop()
