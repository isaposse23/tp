import tkinter as tk
def main ():
             import tkinter as tk  
             from urllib.request import urlopen  
             from PIL import Image, ImageTk  
             from io import BytesIO
             
def descargarFondo():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read() 
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarportada ():
    urlImagen = "https://github.com/isaposse23/imagen/blob/main/Presentaci%C3%B3n%20Diapositivas%20Inform%C3%A1tica%20y%20Tecnolog%C3%ADa%20Ilustrado%20Moderno%20Verde%20Oscuro.png"
    datosImagen = urlopen (urlImagen)
    imagenBinaria = datosImagen.read ()
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

ventana = tk. Tk ()
ventana. title ("isa y lu")
ventana. geometry ("20x1")
ventana.configure (bg="blue")
ventana.mainlop ()

limpiarVentana ()
label = tl.Label (ventana, text= ("volver"), font=("Arial", 12)), command
label.pack (pady=20)

boton_volver = tk.Button (Ventana_text ("volver"), font=("Arial", 12), command=mostrarMenu)
boton_volver.pack(pady=10)

def limpiarVentana ():
     for widget in ventana.winfo_children():  
        
        widget.destroy()

        
def mostrarMenu():
    
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Opción 1", font=("Arial", 14), width=20, command=mostrarOpcion1)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Opción 2", font=("Arial", 14), width=20, command=mostrarOpcion2)
    boton2.pack(pady=10)

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("400x300")
    ventana.title("Menú Centrado")

   
    mostrarMenu()

    ventana.mainloop()
                  
if __name__=="__main__":
    main()
