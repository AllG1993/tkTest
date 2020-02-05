from tkinter import *
from tkinter.ttk import Combobox

# отрисовываем окно и название окна
window = Tk()
window.title("PeripheryX")
# задаем размеры окна и почему-то сдесь же задаем текст

# текст "Введите данные"
enter_data = Label(window.geometry('500x400'), text='Введите данные')
enter_data.grid(column=1, row=0)

# лейбл серийный номер
sn = Label(window, text='Введите С/Н гарнитуры')
sn.grid(column=0, row=1)

# лейбл рабочее место
rm = Label(window, text='Введите РМ')
rm.grid(column=0, row=2)

# лейбл поломка
rm = Label(window, text='Неисправность')
rm.grid(column=0, row=3)


# меняем текст при нажатии кнопки
def click():
    user_data = 'Добавлена гарнитура {}'.format(user_text_sn.get()) + ' c РМ№{}.'.format(user_text_rm.get())
    str(enter_data)
    enter_data.configure(text=user_data)
    res()


def res():
    get_user_data = user_text_sn.get() + '\n' + user_text_rm.get() + '\n' + breakdown_list.get()
    str(get_user_data)
    print(get_user_data)


btn_sn = Button(window, text='Добавить периферию', command=click)
btn_sn.grid(column=1, row=4)


# создаем текстовое поле для кожаного

# поле ввода серийного номера
user_text_sn = Entry(window, width=22)
user_text_sn.grid(column=1, row=1)
user_text_sn.focus()

# поле ввода рабочего места
user_text_rm = Entry(window, width=22)
user_text_rm.grid(column=1, row=2)

# выпадающий список и поломками
breakdown_list = Combobox(window)
breakdown_list['values'] = ('Укажите из списка',
                            'Микрофон',
                            'Левый наушник',
                            'Правый наушник',
                            'Повряждение кабеля')
breakdown_list.current(0)
breakdown_list.grid(column=1, row=3)


window.mainloop()