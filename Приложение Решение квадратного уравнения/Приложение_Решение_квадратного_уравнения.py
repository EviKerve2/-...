from tkinter import*#Имортируем это для окна
from math import *
def lol():#Это все для одной кнопки
    global a,b,c
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if (a.get()==0 and b.get()==0 and c.get()==0):
            sutsav.configure(text=f"D={D}\n{t}")
            a.configure(bg="red")#Если будут одни 0, то эти окна будут красними
            b.configure(bg="red")#Если будут одни 0, то эти окна будут красними
            c.configure(bg="red")#Если будут одни 0, то эти окна будут красними
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)#Это решение
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)#Это решение
                t=f"X1={x1_}, \nX2={x2_}"
                flag=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)#Это решение
                t=f"X1={x1_}"
                flag=True
            elif a==0:
                t="Корней нет"
                flag=False
                a.configure(bg="lightblue")
            elif b==0:
                b_=round((c_/b_),2)
                t=f"X1={b_}"
                flag=True
        else:
            t="Корней нет"
            flag=False
            sutsav.configure(text=f"D={D}\n{t}")
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")#Если в окне не будет ничего написано, то окно будет красным
        if b.get()=="":
            b.configure(bg="red")#Если в окне не будет ничего написано, то окно будет красным
        if c.get()=="":
            c.configure(bg="red")#Если в окне не будет ничего написано, то окно будет красным

aken=Tk()
aken.title("Квадратные уравнения")#название окна
aken.geometry("620x200")#размер окна

lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue",justify=CENTER)#Здесь делаем вид и чтобы мы могли видеть что написано, но не менять, команда Label в этом нам помогает
lbl.pack()
sutsav=Label(aken,text="Ответ",width=60,font="Calibri 26",fg="green",bg="yellow")#Здесь делаем вид и чтобы мы могли видеть что написано, но не менять, команда Label в этом нам помогает
sutsav.pack(side=BOTTOM)#Это для место положения надписи, ну и срабатывании кнопки
a=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")#Здесь делаем вид и чтобы мы могли что нибудь в этом окне написать что нибудь, команда Entry в этом нам помогает
a.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
x1=Label(aken,text="x**2+",font="Calibri 26",fg="green")#Здесь делаем вид и чтобы мы могли видеть что написано, но не менять, команда Label в этом нам помогает
x1.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
b=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")#Здесь делаем вид и чтобы мы могли что нибудь в этом окне написать что нибудь, команда Entry в этом нам помогает
b.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
x2=Label(aken,text="x+",font="Calibri 26",fg="green")#Здесь делаем вид и чтобы мы могли видеть что написано, но не менять, команда Label в этом нам помогает
x2.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
c=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")#Здесь делаем вид и чтобы мы могли что нибудь в этом окне написать что нибудь, команда Entry в этом нам помогает
c.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
o=Label(aken,text="=0",font="Calibri 26",fg="green")#Здесь делаем вид и чтобы мы могли видеть что написано, но не менять, команда Label в этом нам помогает
o.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки

btn=Button(aken,text="Решить", font="Calibri 26",bg="green",command=lol)#Тут делаем вид кнопки и её применение
btn.pack(side=LEFT)#Это для место положения надписи, ну и срабатывании кнопки
grafik=Button(aken,text="График",font="Arial 20",fg="black",bg="green",relief=GROOVE) #Тут делаем вид кнопки и её применение
grafik.pack(side=RIGHT)#Это для место положения надписи, ну и срабатывании кнопки

aken.mainloop()#Я не помню чо это, но это нужно для окна