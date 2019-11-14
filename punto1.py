import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time
cont=0
cont1=100
prom=0

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
led = placa.get_pin('d:8:o')
led1 = placa.get_pin('d:9:p')
led5 = placa.get_pin('d:10:p')
led6 = placa.get_pin('d:11:p')
led7 = placa.get_pin('d:12:o')
led8 = placa.get_pin('d:13:o')

time.sleep(0.1)
ventana = Tk()
ventana.geometry('800x600')
ventana.title("Parcial")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Labing/Documents/Parcial/key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-314e7.firebaseio.com/'
})


frame1 = Frame(ventana, bg="pink", highlightthickness=1, width=1280, height=800, bd= 5)
frame1.place(x = 0,y = 0)

valor= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot1=StringVar()
valor1= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot2=StringVar()
valor2= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot3=StringVar()



def pot_A0():
    global prom
    i=1
    prom=0
    
    #while i<1:
        #i=i+1
    x=a_0.read()
    print(x)
    pot1.set(x)
    #prom=x+prom
    ventana.update()
    time.sleep(0.1)
        
    ref = db.reference('sensor')
    ref.update({
            
        'sensor1/pot1': x
    })

def pot_A1():
    global prom
    i=0
    prom=0
    
    while i<1:
        i=i+1
        x=a_1.read()
        print(x)
        pot2.set(x)
        #prom=x+prom
        ventana.update()
        time.sleep(0.1)
        ref = db.reference('sensor')
        ref.update({
        'sensor1/pot2': x
    })
   

def pot_A2():
    global prom
    i=0
    prom=0
    
    while i<1:
        i=i+1
        x=a_2.read()
        print(x)
        pot3.set(x)
        #prom=x+prom
        ventana.update()
        time.sleep(0.1)
        ref = db.reference('sensor')
        ref.update({
        'sensor1/pot3': x
    })

valor.configure(textvariable=pot1)
valor.place(x=20, y=30)
bot1=Button(text="pot_A0",command=pot_A0)
bot1.place(x=120, y=36)

valor2.configure(textvariable=pot2)
valor2.place(x=20, y=60)
bot2=Button(text="pot_A1",command=pot_A1)
bot2.place(x=120, y=70)

valor1.configure(textvariable=pot3)
valor1.place(x=20, y=90)
bot3=Button(frame1,text="pot_A2",command=pot_A2)
bot3.place(x=114, y=94)


ventana.mainloop()
