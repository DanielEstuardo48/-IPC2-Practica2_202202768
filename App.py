from flask import Flask, render_template
import tkinter as tk
from tkinter import ttk
import webbrowser
import threading
from tkinter import messagebox

class Usuario:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

Usuarios = []

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el archivo HTML 'index.html'
    return render_template('index.html', Usuarios = Usuarios)

def iniciar():
    app.run()

def abrir_nav():
    webbrowser.open_new('http://127.0.0.1:5000')

def start_server():
    threading.Thread(target=iniciar).start()
    threading.Timer(1, abrir_nav).start()

def datos():
    nombre=entrada_nombre.get()
    correo = entrada_correo.get()
    nit = entrada_nit.get()

    if nombre.strip() and correo.strip():
        if nit not in [usuario.nit for usuario in Usuarios]:
            Usuarios.append(Usuario(nombre,correo,nit))
            print("Datos guardados:", Usuarios)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            entrada_nombre.delete(0, tk.END)
            entrada_correo.delete(0, tk.END)
            entrada_nit.delete(0, tk.END)
            Frame_formulario.destroy()
        else:
            messagebox.showerror("Error", "El NIT ya está registrado.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

def formulario():
    global Frame_formulario
    Frame_formulario = tk.Tk()
    Frame_formulario.title('Formulario')
    Frame_formulario.geometry("550x450+450+130")

    LabelRegistro = tk.Label(Frame_formulario, text='REGISTRO DE CLIENTE', font=("Comic Sans MS", 30))
    LabelRegistro.place(x=40, y=18)

    frame_datos = tk.LabelFrame(Frame_formulario, text="Datos Personales")
    frame_datos.pack(padx=10, pady=10)
    frame_datos.place(x=110,y=110)
    

    #! Nombre
    labelnombre = tk.Label(frame_datos, text="Nombre: ", font=("Comic Sans MS", 12))
    labelnombre.grid(row=0, column=0, padx=7, pady=15, sticky="e")
    global entrada_nombre
    entrada_nombre = tk.Entry(frame_datos)
    entrada_nombre.grid(row=0,column=1, padx=7, pady=15)

    #! Correo
    labelnombre = tk.Label(frame_datos, text="Correo Electronico: ", font=("Comic Sans MS", 12))
    labelnombre.grid(row=1, column=0, padx=7, pady=15, sticky="e")
    global entrada_correo
    entrada_correo = tk.Entry(frame_datos)
    entrada_correo.grid(row=1,column=1, padx=7, pady=15)

    #! Nit
    labelnombre = tk.Label(frame_datos, text="Nit: ", font=("Comic Sans MS", 12))
    labelnombre.grid(row=2, column=0, padx=7, pady=15, sticky="e")
    global entrada_nit
    entrada_nit = tk.Entry(frame_datos)
    entrada_nit.grid(row=2,column=1, padx=7, pady=15)

    style = ttk.Style()
    style.configure('Estilog.TButton', foreground='black', font=('Comic Sans MS', 12))
    boton_guardar = ttk.Button(Frame_formulario, text="Registrar", command=datos, style='Estilog.TButton', cursor="hand2")
    boton_guardar.place(x=210,y=330)



#! Se crea Frame principal
root = tk.Tk()
root.title('Inicio')
root.geometry("350x250+630+200")

#! Imagen boton de nuevo usuario
imagen = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Practica2_202202768/user.png')
ancho = 15
alto = 15
imagen_reducida = imagen.subsample(ancho,alto)

#! Imagen boton de navegador
imagenn = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Practica2_202202768/navegador.png')
ancho = 15
alto = 15
imagenn_reducida = imagenn.subsample(ancho,alto)

#!Estilo de boton
style = ttk.Style()
style.configure('Estilo.TButton', foreground='black', font=('Helvetica', 12, 'bold'))


#! Botones de Frame principal
#* Boton de NUsuario
boton = ttk.Button(root, text="Registrar Cliente", cursor="hand2", style='Estilo.TButton', compound=tk.LEFT, image=imagen_reducida, command=formulario)
boton.pack(pady=30)
#* Boton de HTML
boton = ttk.Button(root, text="Abrir el Navegador", cursor="hand2", command=start_server, style='Estilo.TButton',compound=tk.LEFT, image=imagenn_reducida)
boton.pack(pady=20)

root.mainloop()