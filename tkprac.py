from tkinter import *

main_w=Tk()

my_e=Entry(main_w,width=10,font=('Arial',30))

my_e.pack(padx=20,pady=20)

label=Label(main_w,text='Enter your name',font=('Times New Roman',30))

label.pack(padx=30,pady=30)

def clik():
    name=my_e.get()
    if name!='':
        label.config(text='hello '+name+' !')
        my_e.delete(0,END)
    else:
        label.config(text='Enter your name')

my_b=Button(main_w,text='submit',command=clik,padx=10,pady=10,)

my_b.pack(pady=10,padx=10)

main_w.mainloop()