from tkinter import*
klik=0
def klikker(event):
    global klik

aken=Tk()
aken.title("Hujna")
aken.geometry("400x600")

nupp=Button(aken,text="Решить",font="Arial 20",fg="lightblue",bg="black",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)

nupp.pack(side=RIGHT)#side=LEFT,TOP,RIGHT

aken.mainloop()
