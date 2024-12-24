import tkinter as tk
import tkinter.font as tkfnt
import Calculator as cltr

import tkinter.messagebox as mg

w1 = tk.Tk()
w1.title('Units Converter')
w1.geometry('600x300')
w1.resizable(False,False)

heading_font =  tkfnt.Font(family = 'Calibri',size = 12,weight = 'bold')
subHeading_font = tkfnt.Font(family = 'Calibri',size = 10,weight = 'bold')

frm1 = tk.Frame(w1,bd = 1,relief = 'raised',width = 250)
frm1.place(x = 10,y = 10)

lb1 = tk.Label(frm1,text = 'BMI Generator',font = heading_font)
lb1.pack(padx = 2,pady = 3,anchor = 'center')

# adding label for entries
lb2 = tk.Label(frm1,text = "Height for BMI",font = subHeading_font)
lb2.pack(padx = 2,pady = 1,anchor = 'center')

e1 = tk.Entry(frm1,font = ('Calibri',10,'bold'))
e1.pack(padx = 2,pady = 3)

lb3 = tk.Label(frm1,text = "Weight for BMI",font = subHeading_font)
lb3.pack(padx = 2,pady = 1,anchor = 'center')

e2 = tk.Entry(frm1,font = ('Calibri',10,'bold'))
e2.pack(padx = 2,pady = 3)

# adding the methods here for defining the functions
def resetVal():

    if e1.get() == '' and e2.get() == '':
        mg.showwarning('Application Warning','The Entry Box is already empty ?')
        
    else:
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)

def provideVal():

    # storing the value to be changed
    val1 = int(e1.get())

    # calculating the required value
    bmiClass = cltr.BMI()
    # end_value = bmiClass.heightinch()

def endresult():
    
    # creating another window for showing up the end result
    bmi = tk.Tk()
    bmi.title('BMI End Result')
    bmi.geometry('250x150')
    bmi.resizable(0,0)

    bmi.mainloop()

t1 = tk.StringVar()
t1.set('Select on Option')

options = [
    'Height in Inches',
    'Height in Metre',
    'Height in CentiMetre',
    'Height in Foots'
]

opt1 = tk.OptionMenu(frm1,t1,*options)
opt1.pack(padx = 2,pady = 3)

btn1 = tk.Button(frm1,text = 'Submit Value',font = ('Calibri',9,'bold'),command = endresult)
btn1.pack(padx = 2,pady = 3,side = 'left')

btn2 = tk.Button(frm1,text = 'Reset Value',font = ('Calibri',9,'bold'),command = resetVal)
btn2.pack(padx = 2,pady = 3,side = 'right')

w1.mainloop()