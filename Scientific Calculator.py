
#importing modules

from math import *
from tkinter import *

#Making Functions(Back-end)

def click(event):
    global val

    t =  event.widget.cget("text")

    a = val.get()
    if t=="=":
         if a.isdigit():
              value = int(a)
         elif "^" in a:
              try:
                  b = a.split("^",1)
                  value = pow(float(b[0]),float(b[1]))
              except:
                  value="Error"
         else:
              try:
                   value = eval(a)
              except:
                   value = "Error"
                   
         val.set(value)
    elif t=="C":
        val.set("")
    else:
        val.set(val.get()+t)
        
def special(event):
     global val
     t =  event.widget.cget("text")
     a = val.get()
     result = ""
     try:
          if t=="sin":
               result = str(sin(float(a)))
          if t=="cos":
               result = str(cos(float(a)))
          if t=="tan":
               result = str(tan(float(a)))
          if t=="arcsin":
               result = str(asin(float(a)))
          if t=="arccos":
               result = str(acos(float(a)))
          if t=="arctan":
               result = str(atan(float(a)))
          if t=="lg":
               result = str(log10(float(a)))
          if t=="ln":
               result = str(log(float(a)))
          if t=="e":
               if a=="":
                    result = str(e)
               else:
                    result = str(exp(float(a)))
          if t=="pi":
               if a=="":
                    result = str(pi)
               else:
                    result = str(pi*float(a))
          if t=="x!":
               result = str(factorial(float(a)))
          if t=="1/x":
               result = str(1/float(a))
          if t=="+/-":
               if "-" in a:
                   result = a[1:]
               else:
                   result = "-"+ a
          if t=="mod":
               result = str(abs(float(a)))
          if t=="sqrt":
              result = str(sqrt(float(a)))
     except:
          result = "Math Error"
     val.set(result)
          
#Making Interface(Front-end)
#size of an app
root=Tk()
root.title("Scientific Calculator")
root.geometry("400x550+450+70")
root.minsize("400","500")
root.maxsize("400","500")
root.config(bg="#c1d0e4")

#Adding Entry

val = StringVar()
val.set("")
screen = Entry(root,textvar=val,font="lucida 30 bold",borderwidth=7,bd=5,relief=RIDGE,state="disabled",disabledbackground="black",disabledforeground="white").pack(fill=X,padx=6,pady=6)

#Adding Buttons

f1 = Frame(root,bg="#c1d0e4")
b1 = Button(f1,text="sin",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b1.pack(pady=5,padx=5)
b1.bind("<Button-1>",special)

b2 = Button(f1,text="cos",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b2.pack(pady=5,padx=5)
b2.bind("<Button-1>",special)

b3 = Button(f1,text="tan",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b3.pack(pady=5,padx=5)
b3.bind("<Button-1>",special)

b4 = Button(f1,text="^",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b4.pack(pady=5,padx=5)
b4.bind("<Button-1>",click)

b5 = Button(f1,text="sqrt",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b5.pack(pady=5,padx=5)
b5.bind("<Button-1>",special)

b6 = Button(f1,text="x!",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b6.pack(pady=5,padx=5)
b6.bind("<Button-1>",special)

b7 = Button(f1,text="1/x",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b7.pack(pady=5,padx=5)
b7.bind("<Button-1>",special)

f1.pack(fill=Y,side=LEFT,ipady=5,pady=5,padx=3)
f2 = Frame(root,bg="#c1d0e4")
b1 = Button(f2,text="arcsin",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b1.pack(pady=5,padx=5)
b1.bind("<Button-1>",special)

b2 = Button(f2,text="arccos",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b2.pack(pady=5,padx=5)
b2.bind("<Button-1>",special)

b3 = Button(f2,text="arctan",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#83f3e6")
b3.pack(pady=5,padx=5)
b3.bind("<Button-1>",special)

b4 = Button(f2,text="7",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b4.pack(pady=5,padx=5)
b4.bind("<Button-1>",click)

b5 = Button(f2,text="4",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b5.pack(pady=5,padx=5)
b5.bind("<Button-1>",click)

b6 = Button(f2,text="1",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b6.pack(pady=5,padx=5)
b6.bind("<Button-1>",click)

b7 = Button(f2,text="+/-",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2)
b7.pack(pady=5,padx=5)
b7.bind("<Button-1>",special)

f2.pack(fill=Y,side=LEFT,ipady=5,pady=5,padx=3)
f3 = Frame(root,bg="#c1d0e4")
b1 = Button(f3,text="lg",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b1.pack(pady=5,padx=5)
b1.bind("<Button-1>",special)

b2 = Button(f3,text="ln",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b2.pack(pady=5,padx=5)
b2.bind("<Button-1>",special)

b3 = Button(f3,text="mod",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b3.pack(pady=5,padx=5)
b3.bind("<Button-1>",special)

b4 = Button(f3,text="8",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b4.pack(pady=5,padx=5)
b4.bind("<Button-1>",click)

b5 = Button(f3,text="5",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b5.pack(pady=5,padx=5)
b5.bind("<Button-1>",click)

b6 = Button(f3,text="2",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b6.pack(pady=5,padx=5)
b6.bind("<Button-1>",click)

b7 = Button(f3,text="0",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b7.pack(pady=5,padx=5)
b7.bind("<Button-1>",click)

f3.pack(fill=Y,side=LEFT,ipady=5,pady=5,padx=3)
f4 = Frame(root,bg="#c1d0e4")
b1 = Button(f4,text="(",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b1.pack(pady=5,padx=5)
b1.bind("<Button-1>",click)

b2 = Button(f4,text="e",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b2.pack(pady=5,padx=5)
b2.bind("<Button-1>",special)

b3 = Button(f4,text="C",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#ff003c")
b3.pack(pady=5,padx=5)
b3.bind("<Button-1>",click)

b4 = Button(f4,text="9",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b4.pack(pady=5,padx=5)
b4.bind("<Button-1>",click)

b5 = Button(f4,text="6",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b5.pack(pady=5,padx=5)
b5.bind("<Button-1>",click)

b6 = Button(f4,text="3",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#b9b9b9")
b6.pack(pady=5,padx=5)
b6.bind("<Button-1>",click)

b7 = Button(f4,text=".",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2)
b7.pack(pady=5,padx=5)
b7.bind("<Button-1>",click)

f4.pack(fill=Y,side=LEFT,ipady=5,pady=5,padx=3)
f5 = Frame(root,bg="#c1d0e4")
b1 = Button(f5,text=")",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b1.pack(pady=5,padx=5)
b1.bind("<Button-1>",click)

b2 = Button(f5,text="pi",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b2.pack(pady=5,padx=5)
b2.bind("<Button-1>",special)

b3 = Button(f5,text="/",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b3.pack(pady=5,padx=5)
b3.bind("<Button-1>",click)

b4 = Button(f5,text="*",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b4.pack(pady=5,padx=5)
b4.bind("<Button-1>",click)

b5 = Button(f5,text="-",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b5.pack(pady=5,padx=5)
b5.bind("<Button-1>",click)

b6 = Button(f5,text="+",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2,bg="#bbdcf2")
b6.pack(pady=5,padx=5)
b6.bind("<Button-1>",click)

b7 = Button(f5,text="=",font="lucida 11 bold",padx=5,width=5,height=2,relief=RIDGE,borderwidth=2)
b7.pack(pady=5,padx=5)
b7.bind("<Button-1>",click)

f5.pack(fill=Y,side=LEFT,ipady=5,pady=5,padx=3)

#Mainloop
root.mainloop()
