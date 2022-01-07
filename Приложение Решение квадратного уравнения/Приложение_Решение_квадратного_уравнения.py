from tkinter import*
from math import *

    

aken=Tk()
aken.title("Квадратные уровнения")
aken.geometry("620x200")


lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue",justify=CENTER)
lbl.pack()
sutsav=Label(aken,text="Ответ",heigh=1,width=60,font="Calibri 26",fg="green",bg="yellow")
sutsav.pack(side=BOTTOM)
a=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
a.pack(side=LEFT)
x1=Label(aken,text="x**2+",font="Calibri 26",fg="green")
x1.pack(side=LEFT)
b=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
b.pack(side=LEFT)
x2=Label(aken,text="x+",font="Calibri 26",fg="green")
x2.pack(side=LEFT)
c=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
c.pack(side=LEFT)
o=Label(aken,text="=0",font="Calibri 26",fg="green")
o.pack(side=LEFT)

vastus=Button(aken,text="Решить",font="Arial 20",fg="black",bg="green",height=2,width=5,relief=GROOVE)#RAISED, SUNKEN
vastus.pack(side=RIGHT)
grafik=Button(aken,text="График",font="Arial 20",fg="black",bg="green",height=2,width=5,relief=GROOVE)#RAISED, SUNKEN
grafik.pack(side=RIGHT)

aken.mainloop()