import tkinter as tk
import tkinter.font as tkfnt
import Calculator as cltr

w1 = tk.Tk()
w1.title('Units Converter')
w1.geometry('600x300')
w1.resizable(False,False)

heading_font =  tkfnt.Font(family = 'Calibri',size = 12,weight = 'bold')

frm1 = tk.Frame(w1,bd = 1,relief = 'raised',width = 250)
frm1.place(x = 10,y = 10)

lb1 = tk.Label(frm1,text = 'BMI Generator',font = heading_font)
lb1.pack(padx = 2,pady = 5,anchor = 'center')

e1 = tk.Entry(frm1,font = ('Calibri',10,'bold'))
e1.pack(padx = 2,pady = 3)

t1 = tk.StringVar()
t1.set('Height in Inches')

options = [
    'Height in Inches',
    'Height in Metre',
    'Height in CentiMetre',
    'Height in Foots'
]

opt1 = tk.OptionMenu(frm1,t1,*options)
opt1.pack(padx = 2,pady = 3)

btn1 = tk.Button(frm1,text = 'Submit Value',font = ('Calibri',9,'bold'))
btn1.pack(padx = 2,pady = 3,side = 'left')

btn2 = tk.Button(frm1,text = 'Reset Value',font = ('Calibri',9,'bold'))
btn2.pack(padx = 2,pady = 3,side = 'right')

w1.mainloop()