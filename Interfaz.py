# Importar las librerías necesarias.
from tkinter import *


i=0
#obtener datos
def obtener(dato):
	global i
	i += 1
	entrada.insert(i, dato)

# resultado
def operacion():
	global i
	ecuacion = entrada.get()
	if i != 0:		
		try:
			result = str(eval(ecuacion))
			entrada.delete(0,END)
			entrada.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			entrada.delete(0,END)
			entrada.insert(0,result)
	else:
		pass

def borrar_todo():
	entrada.delete(0,END)

def borrar_uno():
	global i


	entrada.delete(i, last=None)
	i -= 1
# Creación de la ventana. 
ventana = Tk() # Esta es la ventana.
ventana.resizable(width=NO, height=NO) # Cambio de tamaño de la ventana (en este caso esta bloqueado).
ventana.config(bg="#212026")
ventana.title("La calculadora más malota.") # este es el titulo de la ventana. 
# Mensaje
texto = Label(ventana) # Esta funcion es para el mensaje
texto.grid(row= 0, column= 0, columnspan= 4, padx= 5, pady= 7)
texto.config(bg= "#d0d0d0", text= 'La calculadora más malota', font= 'Courier 15 italic bold') # configuracion del mensaje.
# caja de entrada.

entrada = Entry(ventana)
entrada.grid(row = 1, column= 0, columnspan= 4)
entrada.config(font='Consolas 20', bg = '#d4e2e5')

# Botones

botonAC = Button(ventana)
botonAC.grid(row= 2, column=0, padx= 2, pady= 2)
botonAC.config(bg="#85848c", text= "AC", font= "Arial 20", width= 4,command= lambda: borrar_uno() )

botonC = Button(ventana)
botonC.grid(row= 2, column=1, padx= 2, pady= 2)
botonC.config(bg="#85848c", text= "C", font= "Arial 20", width= 4, command= lambda: borrar_todo())

botonparentesis1 = Button(ventana)
botonparentesis1.grid(row= 2, column=2, padx= 2, pady= 2)
botonparentesis1.config(bg="#2b2a30", text= "(", font= "Arial 20", width= 4, command=lambda: obtener("("))

botonparentesis2 = Button(ventana)
botonparentesis2.grid(row= 2, column=3, padx= 2, pady= 2)
botonparentesis2.config(bg="#2b2a30", text= ")", font= "Arial 20", width= 4, command=lambda: obtener(")"))

boton7 = Button(ventana)
boton7.grid(row= 3, column=0, padx= 2, pady= 2)
boton7.config(bg="#d4e2e5", text= "7", font= "Arial 20", width= 4, command=lambda: obtener(7))

boton8 = Button(ventana)
boton8.grid(row= 3, column=1, padx= 2, pady= 2)
boton8.config(bg="#d4e2e5", text= "8", font= "Arial 20", width=4, command=lambda: obtener(8))

boton9 = Button(ventana)
boton9.grid(row= 3, column=2, padx= 2, pady= 2)
boton9.config(bg="#d4e2e5", text= "9", font= "Arial 20",width=4, command=lambda: obtener(9))

boton4 = Button(ventana)
boton4.grid(row= 4, column=0, padx= 2, pady= 2)
boton4.config(bg="#d4e2e5", text= "4", font= "Arial 20",width=4, command=lambda: obtener(4))

boton5 = Button(ventana)
boton5.grid(row= 4, column=1, padx= 2, pady= 2)
boton5.config(bg="#d4e2e5", text= "5", font= "Arial 20",width=4, command=lambda: obtener(5))

boton6 = Button(ventana)
boton6.grid(row= 4, column=2, padx= 2, pady= 2)
boton6.config(bg="#d4e2e5", text= "6", font= "Arial 20",width=4, command=lambda: obtener(6))

boton1 = Button(ventana)
boton1.grid(row= 5, column=0, padx= 2, pady= 2)
boton1.config(bg="#d4e2e5", text= "1", font= "Arial 20",width=4, command=lambda: obtener(1))

boton2 = Button(ventana)
boton2.grid(row= 5, column=1, padx= 2, pady= 2)
boton2.config(bg="#d4e2e5", text= "2", font= "Arial 20",width=4, command=lambda: obtener(2))

boton3 = Button(ventana)
boton3.grid(row= 5, column=2, padx= 2, pady= 2)
boton3.config(bg="#d4e2e5", text= "3", font= "Arial 20",width=4, command=lambda: obtener(3))

boton0 = Button(ventana)
boton0.grid(row= 6, column=0, padx= 2, pady= 2)
boton0.config(bg="#d4e2e5", text= "0", font= "Arial 20",width=4, command=lambda: obtener(0))

botonpunto = Button(ventana)
botonpunto.grid(row= 6, column=1, padx= 2, pady= 2)
botonpunto.config(bg="#d4e2e5", text= "·", font= "Arial 20",width=4, command=lambda: obtener('.'))


botonigual = Button(ventana)
botonigual.grid(row= 6, column=2, padx= 2, pady= 2)
botonigual.config(bg="#2b2a30", text= "=", font= "Arial 20",width=4, command=lambda: operacion())


botonmas = Button(ventana)
botonmas.grid(row= 6, column=3, padx= 2, pady= 2)
botonmas.config(bg="#2b2a30", text= "+", font= "Arial 20",width=4, command=lambda: obtener('+'))

botonmenos = Button(ventana)
botonmenos.grid(row= 5, column=3, padx= 2, pady= 2)
botonmenos.config(bg="#2b2a30", text= "-", font= "Arial 20",width=4, command=lambda: obtener('-'))

botonmultiplicacion = Button(ventana)
botonmultiplicacion.grid(row= 4, column=3, padx= 2, pady= 2)
botonmultiplicacion.config(bg="#2b2a30", text= "*", font= "Arial 20",width=4, command=lambda: obtener('*'))

botondiv = Button(ventana)
botondiv.grid(row= 3, column=3, padx= 2, pady= 2)
botondiv.config(bg="#2b2a30", text= "/", font= "Arial 20",width=4, command=lambda: obtener('/'))
 
 

# etiqueta del creador
eti = Label(ventana)
eti.grid(row=7, column=3,padx = 2)
eti.config(bg ='#d0d0d0',text = 'BY MilfuegosxDD', font= 'Arial 6 italic', width= 14)


ventana.mainloop()