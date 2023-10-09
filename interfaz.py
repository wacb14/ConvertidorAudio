import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from tkinter import messagebox
from convertidor import convertir
import os

def comprobarArchivo(ruta):
    if(os.path.exists(ruta)):
        return True
    else:
        return False
# Función que se ejecutará cuando se haga clic en el botón
def procesar_archivos():
    archivo1=entry1.get()
    archivo2=entry2.get()
    archivo3=entry3.get()
    if(archivo1!="" and archivo2!="" and archivo3!=""):
        if(comprobarArchivo(archivo1) and comprobarArchivo(archivo2) and comprobarArchivo(archivo3)):
            convertir(entry1.get(), entry2.get(), entry3.get())
            messagebox.showinfo("Exito!!", "Los archivos se han procesado correctamente!")        
            limpiarInterfaz()
        else:
            messagebox.showinfo("Advertencia!", "Revisa que los campos de archivos sean correctos y vuelve a intentarlo")        
    else:
        messagebox.showinfo("Advertencia!", "Rellena los 3 campos de archivos y vuelve a intentarlo")

def limpiarEntry(campo):
    campo.config(state='normal')
    campo.delete(0, tk.END)

def limpiarInterfaz():
    limpiarEntry(entry1)
    if (not (checkbox_var.get())):
        limpiarEntry(entry2)
    limpiarEntry(entry3)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Convertidor personalizado')
ventana.config(bg="#FFC04D")

#  Obtenemos el largo y  ancho de la pantalla
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 500
hventana = 500

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
ventana.geometry(str(wventana)+'x'+str(hventana) +
                 '+'+str(pwidth)+'+'+str(pheight))

# Función para abrir el cuadro de diálogo de selección de archivos y guardar el resultado en el campo de entrada correspondiente


def abrir_dialogo(campo):
    archivo = filedialog.askopenfilename(
        title='Selecciona un archivo',
        filetypes=[('Todos los archivos', '*.*')]
    )
    if archivo:
        campo.delete(0, tk.END)
        campo.insert(0, archivo)
        campo.config(state='readonly')


# Crear campos de entrada de archivos
entry1 = tk.Entry(ventana, width=60)
entry2 = tk.Entry(ventana, width=60)
entry3 = tk.Entry(ventana, width=60)

# Crear botones para abrir el cuadro de diálogo de selección de archivos
boton1 = tk.Button(ventana, text='Seleccionar Archivo 1',
                   command=lambda: abrir_dialogo(entry1), bg='#297BE0', fg='white', font=("Verdana", 11))
boton2 = tk.Button(ventana, text='Seleccionar Archivo 2',
                   command=lambda: abrir_dialogo(entry2), bg='#297BE0', fg='white', font=("Verdana", 11))
boton3 = tk.Button(ventana, text='Seleccionar Archivo 3',
                   command=lambda: abrir_dialogo(entry3), bg='#297BE0', fg='white', font=("Verdana", 11))
# Chekbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(ventana, text="Mantener", variable=checkbox_var)
checkbox.config(bg="#FFC04D", fg="#004394", font=("Verdana", 12))

# Crear un botón para procesar los archivos
boton_procesar = tk.Button(
    ventana, text='Procesar Archivos', command=procesar_archivos, bg='#004394', fg='white', font=("Verdana", 12))

img_boton = tk.PhotoImage(file="refresh.png")
boton_refresh = tk.Button(image=img_boton, bg='#E0A12D',
                          command=lambda: limpiarInterfaz())

# Labels
titulo = Label(ventana, text="CONVERTIDOR")
titulo.config(bg="#FFC04D", fg="#004394", font=("Verdana", 20))

# Ubicar los elementos en la ventana
boton_refresh.place(x=400, y=20)
posicion = 60
titulo.place(x=160, y=posicion)
posicion += 50
entry1.place(x=70, y=posicion)
posicion += 35
boton1.place(x=170, y=posicion)
posicion += 55
entry2.place(x=70, y=posicion)
posicion += 35
boton2.place(x=100, y=posicion)
checkbox.place(x=290, y=posicion)
posicion += 55
entry3.place(x=70, y=posicion)
posicion += 35
boton3.place(x=170, y=posicion)
posicion += 120
boton_procesar.place(x=175, y=posicion)

# Iniciar el ciclo principal de la interfaz gráfica
ventana.mainloop()
