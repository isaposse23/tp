import tkinter as tk
def main ():
             import tkinter as tk  # Tkinter para la ventana
             from urllib.request import urlopen  # Para descargar la imagen desde internet
             from PIL import Image, ImageTk  # Pillow para trabajar con imágenes
             from io import BytesIO  # Para convertir los datos de la imagen


# Paso 1: Descargar la imagen de internet
def descargarFondo():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarportada ():
    urlImagen = "https://github.com/isaposse23/imagen/blob/main/Presentaci%C3%B3n%20Diapositivas%20Inform%C3%A1tica%20y%20Tecnolog%C3%ADa%20Ilustrado%20Moderno%20Verde%20Oscuro.png"
    datosImagen = urlopen (urlImagen) # Descargar la portada
    imagenBinaria = datosImagen.read () # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
#crear ventana principal
ventana = tk. Tk ()
ventana. title ("isa")
ventana. geometry ("20x1")
ventana configure (bg="blue")
ventana.mainlop ()

def mostrarOpcion1 ()
limpiarVentana ()
label = tl.Label (ventana, text= "volver", font=("Arial", 12), command
label.pack (pady=20)

boton_volver = tk.Button (ventana_ text "volver", font=( "Arial", 12), command
boton_volver.pack (pady=10)

def limpiarVentana ():
    #
                  
if __name__=="__main__":
    main()
