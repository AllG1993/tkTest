from tkinter import *


window = Tk()
window.title("PeripheryX")

lbl = Label(window.geometry('400x250'), text='Программа учета периферии')
lbl.grid(column=0, row=0)

btn_add = Button(window, text='Добавить периферию')
btn_add.grid(column=0, row=2)

window.mainloop()