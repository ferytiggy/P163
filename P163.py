# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:18:32 2024

@author: Aidan
"""

from tkinter import*
from tkinter.messagebox import*

root = Tk()
root.title("P163")
root.geometry("600x600")

pregunta_1_boton = StringVar(value="0")
pregunta_1 = Label(root, text="Te hidratas muy bien?" )
pregunta_1.pack()
respuesta_1 = Radiobutton(root, text="si", variable=pregunta_1_boton, value="si")
respuesta_1.pack()
respuesta_2 = Radiobutton(root, text="no", variable=pregunta_1_boton, value="no")
respuesta_2.pack()

pregunta_2_boton = StringVar(value="0")
pregunta_2 = Label(root, text="Comes toda tu porción?")
pregunta_2.pack()
respuesta_3 = Radiobutton(root, text="si", variable=pregunta_2_boton, value="si")
respuesta_3.pack()
respuesta_4 = Radiobutton(root, text="no", variable=pregunta_2_boton, value="no")
respuesta_4.pack()

pregunta_3_boton = StringVar(value="0")
pregunta_3 = Label(root, text="Comes vegetales?")
pregunta_3.pack()
respuesta_5 = Radiobutton(root, text="si", variable=pregunta_3_boton, value="si")
respuesta_5.pack()
respuesta_6 = Radiobutton(root, text="no", variable=pregunta_3_boton, value="no")
respuesta_6.pack()

def puntuacion():
    score=0
    if pregunta_1_boton.get()=="si":
        score = score+20
        print(score)
    if pregunta_2_boton.get()=="si":
        score = score+20
        print(score)
    if pregunta_3_boton.get()=="si":
        scire = score+20
        print(score)
    if score<=20:
        showinfo("Reporte", "Necesitas cambiar tus habitos ya mismo, estas dañando tu cuerpo")
    elif score>20 and score<=40:
        showinfo("Reporte", "Estas haciendolo bien pero necesitas mejorar")
    else: showinfo("Reporte", "Vas por buen camino, eres muy saludable")
    
boton = Button(root,  text="reporte",command=puntuacion)
boton.pack()

root.mainloop()