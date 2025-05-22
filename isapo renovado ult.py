import tkinter as tk

from urllib.request import urlopen  
from PIL import Image, ImageTk  
from io import BytesIO

def descargarImagenPortada ():
    urlImagen= "https://i.pinimg.com/1200x/8d/04/a1/8d04a16d292cab911b2965df05482bb2.jpg"
    datosImagen= urlopen(urlImagen)
   imagenBinaria = datosImagen.read()
   imagen= Image.open (BytesIO(imagenBinaria))
   imagen de retorno 
   return imagen
def descargarImagenFondo():
    urlImagen = "https://cdn0.bodas.net/article/9777/3_2/1280/jpg/7779-fiyi.jpeg"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()
    Imagen = Image.open (BytesIO(imagenBinaria))
    return imagen
def descargarImagenFlorDeLoto
    urlImagen =  "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2023/05/18/16844329023209.jpg"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read() 
    Imagen = Image.open (BytesIO(imagenBinaria))
    return imagen

def descargarImagenFlorMargarita
    urlImagen =  "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-WcBl5RxMNuusOGnzsAp1xlecATGJWTDNa6-tBgdKz8fTSLI8VW1o0MyFkhKf-lXM4aV2-dk6WUKRFkI2n9sM-IXmZ00MxH0Czayy4KXuyAGyvitj6DNbfTth7Nh1eqe9EhId8i9QXWs/s1600/IMG_5980.jpeg"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read() 
    Imagen = Image.open (BytesIO(imagenBinaria))
    return imagen

def descargarImagenFlorTulipan
    urlImagen =  "https://bruflor.es/blog/wp-content/uploads/2020/01/tulipan.jpg"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read() 
    Imagen = Image.open (BytesIO(imagenBinaria))
    return imagen

def descargarImagenFlorHibiscusHawaiana
    urlImagen =  "https://verdecora.es/blog/wp-content/uploads/2020/06/como-cultivar-hibiscus.jpg"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read() 
    Imagen = Image.open (BytesIO(imagenBinaria))
    return imagen

    def mostrarOpcion1():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion2():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)
    
def mostrarOpcion3():
    limpiarVentana()
    label = tk.Label(ventana, text= "Elegiste la Opción 3", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion4():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 4", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
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
    
    boton3 = tk.Button(ventana, text="Opción 3", font=("Arial", 14), width=20, command=mostrarOpcion3)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Opción 4", font=("Arial", 14), width=20, command=mostrarOpcion4)
    boton4.pack(pady=10)

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("100x300")
    ventana.title("el menu esta cerrado")

imagen=descargarImagenPortada ()
imagenRedimensionada = imagen. resize ((ancho, alto), Image

    mostrarMenu()

    ventana.mainloop()

if __name__=="__main__":
    main()
