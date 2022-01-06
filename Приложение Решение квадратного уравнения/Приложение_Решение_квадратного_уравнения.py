from tkinter import*
klik=0
def klikker(event):
    global klik

aken=Tk()
aken.title("Квадратные уровнения")
aken.geometry("600x300")

nupp=Button(aken,text="Решить",font="Arial 20",fg="black",bg="green",height=2,width=10,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)

nupp.pack(side=RIGHT)#side=LEFT,TOP,RIGHT

aken.mainloop()
