from tkinter import *
import random
root=Tk()
root.title()
yourscore=0
computerscore=0
def data():
    score.set(0)
    cscore.set(0)
def rock():
    global yourscore
    global computerscore
    global Textarea
    Textarea.insert(END,b"Your Choice:Rock\n")
    ans=random.choice(['rock','paper','scisoor'])
    Textarea.insert(END,f"Computer's Choice:{ans}\n")
    if((ans=='rock' or ans=='paper') or (ans=='rock' and ans=='scisoor')):
        computerscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "Computer Wins\n")
        cscore.set(computerscore)
    else:
        yourscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "You Wins\n")
        score.set(yourscore)

def Scissiors():
    global yourscore
    global computerscore
    global Textarea
    Textarea.insert(END, "Your Choice:Scissiors\n")
    ans = random.choice(['rock', 'paper', 'scisoor'])
    Textarea.insert(END, f"Computer's Choice:{ans}\n")
    if ((ans == 'rock' and ans == 'paper') or (ans == 'rock' or ans == 'scisoor')):
        computerscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "Computer Wins\n")
        cscore.set(computerscore)
    else:
        yourscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "You Wins\n")
        score.set(yourscore)
def Paper():
    global yourscore
    global computerscore
    global Textarea
    Textarea.insert(END, "Your Choice:Paper\n")
    ans = random.choice(['rock', 'paper', 'scisoor'])
    Textarea.insert(END, f"Computer's Choice:{ans}\n")
    if ((ans == 'scisoor' or ans == 'paper')):
        computerscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "Computer Wins\n")
        cscore.set(computerscore)
    else:
        yourscore += 1
        Textarea.insert(END, f"Your Score:{yourscore}\n")
        Textarea.insert(END, f"computer score:{computerscore}\n")
        Textarea.insert(END, "You Wins\n")
        score.set(yourscore)
score=IntVar()
cscore=IntVar()
Button1=Button(root,text="Rock",font="comicsansms 19 bold",command=rock,bg="red")
Button1.place(x=400,y=120)
Button2=Button(root,text="Scissiors",font="comicsansms 19 bold",command=Scissiors,bg="yellow")
Button2.place(x=550,y=120)
Button3=Button(root,text="Paper",font="comicsansms 19 bold",command=Paper,bg="blue")
Button3.place(x=750,y=120)
Textarea=Text(root,font="comicsansms 19 bold",relief=SUNKEN,bg="yellow",fg="red")
Textarea.place(x=310,y=280)
xscrollbar=Scrollbar(Textarea,orient=VERTICAL)
xscrollbar.pack(side="right",fill=Y)
Textarea=Text(Textarea,xscrollcommand=xscrollbar.set)
Textarea.pack()
xscrollbar.config(command=Textarea.yview())


label=Label(root,text="Your Score",font="comicsansms 14 bold")
label.place(x=950,y=120)
entry=Entry(root,textvariable=score,font="comicsansms 18 bold",width=5)
entry.place(x=970,y=145)
label1=Label(root,text="Computer Score",font="comicsansms 14 bold")
label1.place(x=1100,y=120)
entry1=Entry(root,textvariable=cscore,font="comicsansms 18 bold",width=5)
entry1.place(x=1100,y=145)
data()

root.mainloop()
