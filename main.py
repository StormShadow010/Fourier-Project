import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import Image, ImageTk
from graphs import *

fourier_commun_functions=["Onda cuadrada","Tren de pulsos rectangulares", "Onda diente de sierra", "Onda triangular", "Función seno rectificado de media onda","Función seno rectificado de onda completa"]
#Functions 
def graph(indice,N,A,T,D):
    if indice==0:
        onda_duadrada(A,T,N)
    elif indice==1:
        tren_de_pulsos_rectangular(A,T,N,D)
    elif indice==2:
        onda_diente_de_sierra(A,T,N)
    elif indice==3:
        onda_triangular(A,T,N)
    elif indice==4:
        funcion_seno_rectificado_de_media_onda(A,T,N)
    elif indice==5:
        funcion_seno_rectificado_de_onda_completa(A,T,N)
    
def selection_changed(event):
    selection = combo.get()
    if selection in fourier_commun_functions:
        indice = fourier_commun_functions.index(selection)
        newWindow = tk.Toplevel(master)
        newWindow.title(selection)
        newWindow.geometry("650x650")
        newWindow.resizable(False, False)
        newWindow.config(bg="#D5E4ED")

        label = tk.Label(newWindow,text =selection,font = ('Roboto', 12,'bold'),bg="#D5E4ED",fg="#16232E")
        label.pack()        
        imagef = Image.open(f"Final Project/images/Commun_functions/{indice}.png")
        imgf = ImageTk.PhotoImage(imagef)
        label1 = tk.Label(newWindow,image=imgf, borderwidth=3, relief="raised")
        label1.imagef = imgf
        label1.pack(pady = 10)   
        imagefor = Image.open(f"Final Project/images/Commun_functions/{indice}.{indice}.png")
        imgfor = ImageTk.PhotoImage(imagefor)
        label2 = tk.Label(newWindow,image=imgfor,borderwidth=3, relief="sunken")
        label2.imagefor = imgfor
        label2.pack(pady = 10) 
        labelN = tk.Label(newWindow,text ="Armonicos",font = ('Roboto', 12,'bold'),bg="#D5E4ED",fg="#302C2C")
        labelN.pack()
        EN = tk.Entry(newWindow,bd =5)
        EN.pack(pady = 2)
        labelA = tk.Label(newWindow,text ="Amplitud",font = ('Roboto', 12,'bold'),bg="#D5E4ED",fg="#302C2C")
        labelA.pack()
        EA = tk.Entry(newWindow,bd =5)
        EA.pack(pady = 2)
        labelT = tk.Label(newWindow,text ="Periodo",font = ('Roboto', 12,'bold'),bg="#D5E4ED",fg="#302C2C")
        labelT.pack()
        ET = tk.Entry(newWindow,bd =5)
        ET.pack(pady = 2)
        
        if indice==1:
            labelD = tk.Label(newWindow,text ="Duracion (τ) (Valor entre 0-100)",font = ('Roboto', 12,'bold'),bg="#D5E4ED",fg="#302C2C")
            labelD.pack()
            ED = tk.Entry(newWindow,bd =5)
            ED.pack(pady = 2)
            botoncalculos = tk.Button(newWindow, text="Gráficar",bg="black",fg="white",activeforeground="blue",activebackground="Orange", command=lambda:graph(indice,int(EN.get()),int(EA.get()),int(ET.get()),int(ED.get())))
        else:
            botoncalculos = tk.Button(newWindow, text="Gráficar",bg="black",fg="white",activeforeground="blue",activebackground="Orange",command=lambda:graph(indice,int(EN.get()),int(EA.get()),int(ET.get()),0))
        botoncalculos.pack(padx=10,pady=10)
#Master window
master = tk.Tk()
master.title("Series de Fourier")
master.geometry("600x500")
master.resizable(False, False)
# Add image file
bg = Image.open("Final Project/wallpapers/w3.jpg")
imgbg = ImageTk.PhotoImage(bg)
# Show image using label
labelwallpaper = tk.Label(master, image = imgbg)
labelwallpaper.place(x = 0,y = 0)
info = tk.Label(master,text ="Esta aplicación permite que\nhagas la serie de fourier de una señal\n la cual puedes seleccionar abajo y así poder\nver su respectiva gráfica.",font = ('Roboto', 12), borderwidth=3, relief="raised", bg="#16232E", fg="#E3C75F").pack(pady=10)

TextSignal = tk.Label(master,text ="Selecciona el tipo de señal:",font = ('Helvetica', 10, 'bold'),borderwidth=3, relief="groove",bg="#164C45", fg="#E3C75F").pack(pady=20)
#ComboBox opciones
combo = ttk.Combobox(values=fourier_commun_functions,width=35)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.pack()

#Imagen que cambia
image = Image.open("Final Project/images/FourierMain.jpg")
resize_image = image.resize((250, 250))
img = ImageTk.PhotoImage(resize_image)
ImageFourier = tk.Label(image=img)
ImageFourier.image = img
ImageFourier.pack(pady = 10)

info2 = tk.Label(master,text ="Recuerda dar los valores en enteros!!!",font = ('Roboto', 12), borderwidth=3, relief="raised", bg="#16232E", fg="#E3C75F").pack(pady=10)

master.mainloop()
#Storm Shadow 010