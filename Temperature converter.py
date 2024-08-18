from tkinter import Tk,Label,Entry,Button
def convertToFah():
    answer=int(e1.get())*9/5+32
    l2=Label(root,text='Equivalent temperature in Fahrenheit is '+str(answer))
    l2.pack()
def convertToKel():
    solution=int(e2.get())+273
    l3=Label(root,text='Equivalent temperature in Kelvin is '+str(solution))
    l3.pack()
root=Tk()
root.minsize(300,200)
root.maxsize(500,400)
root.title('Temperature Converter')
l1=Label(root,text='Enter temperature in Celsius to convert: ')
l1.pack()
l4=Label(root,text='Celsius to Fahrenheit : ')
l4.pack()
e1=Entry(root)
e1.pack()
b1=Button(root,text='Convert',command=convertToFah)
b1.pack()
l5=Label(root,text='Celsius to Kelvin : ')
l5.pack()
e2=Entry(root)
e2.pack()
b2=Button(root,text='Convert',command=convertToKel)
b2.pack()
root.mainloop()

