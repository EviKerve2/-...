from tkinter import*
from math import *
import matplotlib.pyplot as plt
import numpy as np

def lol():    
    flag=""
    D=0
    t=""
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
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
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return flag,D,t

def kliik(event):
    aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+400))

def kliikut(event):
    aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-400))

def graafik():
    flag,D,t=lol()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    sutsav.configure(text=f"D={D}\n{t}\n{text}")

def whale():
    x1=np.arange(0, 9.5, 0.5) 
    y1=(2/27)*x1*x1-3 
    x2=np.arange(-10, 0.5, 0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6 
    x5=np.arange(5, 9, 0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5, 8.3, 0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13, -8.5, 0.5)  
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15, -9.5, 0.5)
    y9=[1]*len(x9)
    x10=np.arange(3, 4, 0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Ruutvõrrand")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def umbrella():
    x = np.linspace(-12,12,100)
    y = -1/18*x**2+12
    plt.plot(x,y,color="r")
    x = np.linspace(-4,4,100)
    y = -1/8*x**2+6
    plt.plot(x,y,color="b")
    x = np.linspace(-12,-4,100)
    y = -1/8*(x+8)**2+6
    plt.plot(x,y,color="g")
    x = np.linspace(4,12,100)
    y = -1/8*(x-8)**2+6
    plt.plot(x,y,color="c")
    x = np.linspace(-4,-0.3,100)
    y = 2*(x+3)**2-9
    plt.plot(x,y,color="m")
    x = np.linspace(-4.5,0.2,100)
    y = 1.5*(x+3)**2-10
    plt.plot(x,y,color="k")
    plt.title("Ruutvõrrand Umbrella")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def glasses():
    x=np.linspace(-9,-1,100)
    y=-(1/16)*(x+5)**2+2
    plt.plot(x,y,color="r")
    x=np.linspace(1,9,100)
    y=-(1/16)*(x-5)**2+2
    plt.plot(x,y,color="b")
    x=np.linspace(-9,-1,100)
    y=(1/4)*(x+5)**2-3
    plt.plot(x,y,color="g")
    x=np.linspace(1,9,100)
    y=(1/4)*(x-5)**2-3
    plt.plot(x,y,color="c")
    x=np.linspace(-9,-6,100)
    y=-(x+7)**2+5
    plt.plot(x,y,color="m")
    x=np.linspace(6,9,100)
    y=-(x-7)**2+5
    x=np.linspace(-1,1,100)
    y=-0.5*x**2+1.5
    plt.plot(x,y,color="k")
    plt.title("Ruutvõrrand Umbrella")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def frog():
    x = np.linspace(-7,7,100)
    y = -3/49*x**2+8
    plt.plot(x,y)
    x = np.linspace(-7,7,100)
    y = 4/49*x**2+1
    plt.plot(x,y)
    x = np.linspace(-6.8,-2,100)
    y = -0.75*(x+4)**2+11
    plt.plot(x,y)
    x = np.linspace(2,6.8,100)
    y = -0.75*(x-4)**2+11
    plt.plot(x,y)
    x = np.linspace(-5.8,-2.8,100)
    y = -1*(x+4)**2+9
    plt.plot(x,y)
    x = np.linspace(2.8,5.8,100)
    y = -1*(x-4)**2+9
    plt.plot(x,y)
    x = np.linspace(-4,4,100)
    y = 4/9*x**2-5
    plt.plot(x,y)
    x = np.linspace(-5.2,5.2,100)
    y = 4/9*x**2-9
    plt.plot(x,y)

    x = np.linspace(-7,-2.8,100)
    y = -1/16*(x+3)**2-6
    plt.plot(x,y)
    x = np.linspace(2.8,7,100)
    y = -1/16*(x-3)**2-6
    plt.plot(x,y)
    x = np.linspace(-7,0,100)
    y = 1/9*(x+4)**2-11
    plt.plot(x,y)
    x = np.linspace(0,7,100)
    y = 1/9*(x-4)**2-11
    plt.plot(x,y)
    x = np.linspace(-7,-4.5,100)
    y = -1*(x+5)**2
    plt.plot(x,y)
    x = np.linspace(4.5,7,100)
    y = -1*(x-5)**2
    plt.plot(x,y)
    x = np.linspace(-3,3,100)
    y = 2/9*x**2+2
    plt.plot(x,y)


    plt.title("Ruutvõrrand frog")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

def butterfly():
    x = np.linspace(-9,-1,100)
    y = -1/8*(x+9)**2+8
    plt.plot(x,y)
    x = np.linspace(1,9,100)
    y = -1/8*(x-9)**2+8
    plt.plot(x,y)
    x = np.linspace(-9,-8,100)
    y = 7*(x+8)**2+1
    plt.plot(x,y)
    x = np.linspace(8,9,100)
    y = 7*(x-8)**2+1
    plt.plot(x,y)
    x = np.linspace(-8,-1,100)
    y = 1/49*(x+1)**2
    plt.plot(x,y)
    x = np.linspace(1,8,100)
    y = 1/49*(x-1)**2
    plt.plot(x,y)

    x = np.linspace(-8,-1,100)
    y = -4/49*(x+1)**2
    plt.plot(x,y)
    x = np.linspace(1,8,100)
    y = -4/49*(x-1)**2
    plt.plot(x,y)
    x = np.linspace(-8,-2,100)
    y = 1/3*(x+5)**2-7
    plt.plot(x,y)
    x = np.linspace(2,8,100)
    y = 1/3*(x-5)**2-7
    plt.plot(x,y)
    x = np.linspace(-2,-1,100)
    y = -2*(x+1)**2-2
    plt.plot(x,y)
    x = np.linspace(1,2,100)
    y = -2*(x-1)**2-2
    plt.plot(x,y)
    x = np.linspace(-1,1,100)
    y = -4*x**2+2
    plt.plot(x,y)
    x = np.linspace(-1,1,100)
    y = 4*x**2-6
    plt.plot(x,y)
    x = np.linspace(-2,0,100)
    y = -1.5*x+2
    plt.plot(x,y)
    x = np.linspace(0,2,100)
    y = 1.5*x+2
    plt.plot(x,y)

    plt.title("Ruutvõrrand Buterfly")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

aken=Tk()
aken.title("Квадратные уравнения")
aken.geometry("620x250")

f1=Frame(aken,width=620,height=250)
f1.pack(side=TOP)

f2=Frame(aken,width=620,height=250)
f2.pack(side=TOP)

lbl=Label(f1,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue",justify=CENTER)
lbl.pack()

sutsav=Label(f1,text="Ответ",width=60,fg="green",bg="yellow")
sutsav.pack(side=BOTTOM)

popa=Button(f1,text="Увеличить окно",font="Calibri 20",height=1,width=15,fg="black",bg="green")
popa.pack(side=BOTTOM)
popa.bind("<Button-1>",kliik)

apop=Button(f1,text="Уменьшить окно",font="Calibri 20",height=1,width=15,fg="black",bg="green")
apop.pack(side=BOTTOM)
apop.bind("<Button-1>",kliikut)

a=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
a.pack(side=LEFT)

x1=Label(f1,text="x**2+",font="Calibri 26",fg="green") 
x1.pack(side=LEFT)

b=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
b.pack(side=LEFT)

x2=Label(f1,text="x+",font="Calibri 26",fg="green")
x2.pack(side=LEFT)

c=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
c.pack(side=LEFT)

o=Label(f1,text="=0",font="Calibri 26",fg="green")
o.pack(side=LEFT)

btn=Button(f1,text="Решить", font="Calibri 26",bg="green",relief=GROOVE, command=lol)
btn.pack(side=RIGHT)

grafik=Button(f1,text="График",font="Calibri 26",fg="black",bg="green",relief=GROOVE,command=graafik) 
grafik.pack(side=RIGHT)

lblll=Label(f2,text="Рисунок",font="Calibri 26",fg="black",justify=CENTER)
lblll.pack()

w1=Radiobutton(f2,text="Кит",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=whale)
w1.pack(side=TOP)

w2=Radiobutton(f2,text="Зонтик",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=umbrella)
w2.pack(side=TOP)

w3=Radiobutton(f2,text="Очки",font="Calibri 26",fg="black",bg="red",relief=GROOVE,command=glasses)
w3.pack(side=TOP)

w4=Radiobutton(f2,text="Лягушка",font="Calibri 26",fg="black",bg="red",relief=GROOVE, command=frog)
w4.pack(side=TOP)

w5=Radiobutton(f2,text="Бабочка",font="Calibri 26",fg="black",bg="red",relief=GROOVE, command=butterfly)
w5.pack(side=TOP)

aken.mainloop()