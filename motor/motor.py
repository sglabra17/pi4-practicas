#Enviando ordenes al Arduino mediante comunicacion Serial para mover un motor
#librerias
import serial
import tkinter as tk

#Objetos
s = serial.Serial("/dev/ttyACM0",9600)

#Funciones
def uno():
    dato = "1"
    s.write(dato.encode())
def dos():
    dato = "2"
    s.write(dato.encode())
def tres():
    dato = "3"
    s.write(dato.encode())
def cuatro():
    dato = "4"
    s.write(dato.encode())

#Cuerpo del Programa
w = tk.Tk()
w.title("Manipulando Motor")

f = tk.Frame(w).grid(row=0,column=0)

lb1 = tk.Label(f,text="Selecciona una Opción").grid(row=0,column=0,columnspan=4)

btn1 = tk.Button(f,text="0 Grados",command=uno,width=20).grid(row=1,column=0)
btn2 = tk.Button(f,text="90 Grados",command=dos,width=20).grid(row=1,column=1)
btn3 = tk.Button(f,text="180 Grados",command=tres,width=20).grid(row=1,column=2)
btn4 = tk.Button(f,text="Giro Completo",command=cuatro,width=20).grid(row=1,column=3)
        
w.mainloop()
s.close()
