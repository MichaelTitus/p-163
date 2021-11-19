from tkinter import *
import random

root=Tk()
root.title("vascular report")
root.geometry("500x500")

q1_rb=StringVar(value="0")
q1=Label(root,text="Do you have shortness of breath?")
q1.pack()
q1_rb1=Radiobutton(root,text="Yes",variable=q1_rb,value="Yes")
q1_rb1.pack()
q1_rb2=Radiobutton(root,text="No",variable=q1_rb,value="No")
q1_rb2.pack()

q2_rb=StringVar(value="0")
q2=Label(root,text="Are you swelling up?")
q2.pack()
q2_rb1=Radiobutton(root,text="Yes",variable=q2_rb,value="Yes")
q2_rb1.pack()
q2_rb2=Radiobutton(root,text="No",variable=q2_rb,value="No")
q2_rb2.pack()

q3_rb=StringVar(value="0")
q3=Label(root,text="Are you having weezing?")
q3.pack()
q3_rb1=Radiobutton(root,text="Yes",variable=q3_rb,value="Yes")
q3_rb1.pack()
q3_rb2=Radiobutton(root,text="No",variable=q3_rb,value="No")
q3_rb2.pack()

def score():
    score=0
    if q1_rb.get()=="Yes":
        score=score+69
    if q2_rb.get()=="Yes":
        score=score+69
    if q3_rb.get()=="Yes":
        score=score+69    
        
    if score<=69:
        messagebox.showinfo("Report","You don't need to go to doctor")
    elif score>69 and score<=138:
        messagebox.showinfo("Report","You better get moving the clocks ticking for you to be saved.")
    else:
        messagebox.showinfo("Report","You better start hiding if you did a prank phone call cause this might be a criminal act and the ambulance is coming. If you are actually in pain pls Rest In Peace")
        
btn=Button(root,text="Look fast if there are more than two yeses",command=score)
btn.pack()


root.mainloop()
