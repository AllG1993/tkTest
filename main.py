from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import db_connection

# отрисовываем окно и название окна
root = Tk()
root.title("PeripheryX")
root.geometry('1200x800')
# меню
menu = Menu(root)
main_menu = Menu(menu, tearoff=0)
main_menu.add_command(label='Параметры сервера')
menu.add_cascade(label='Меню', menu=main_menu)
root.config(menu=menu)

# текст "Введите данные"
enter_data = Label(text='Введите данные')
enter_data.grid(column=1, row=0)

# лейбл серийный номер
sn = Label(root, text='Введите С/Н гарнитуры: ')
sn.grid(column=0, row=1, sticky=E)

# лейбл рабочее место
rm = Label(root, text='Введите РМ: ')
rm.grid(column=0, row=2, sticky=E)

# лейбл поломка
rm = Label(root, text='Неисправность: ')
rm.grid(column=0, row=3, sticky=E)


# меняем текст при нажатии кнопки
def click():
    user_data = 'Добавлена гарнитура {}'.format(user_text_sn.get()) + ' c РМ№{}.'.format(user_text_rm.get())
    str(enter_data)
    enter_data.configure(text=user_data)
    insert_data()


btn_sn = Button(root, text='Добавить периферию', command=click)
btn_sn.grid(column=1, row=4)


# создаем текстовое поле для кожаного

# поле ввода серийного номера
user_text_sn = Entry(root, width=22)
user_text_sn.grid(column=1, row=1)
user_text_sn.focus()

# поле ввода рабочего места
user_text_rm = Entry(root, width=22)
user_text_rm.grid(column=1, row=2)

# выпадающий список и поломками
breakdown_list = Combobox(root)
breakdown_list['values'] = ('Укажите из списка',
                            'Микрофон',
                            'Левый наушник',
                            'Правый наушник',
                            'Повряждение кабеля')
breakdown_list.current(0)
breakdown_list.grid(column=1, row=3)

# создаем cursor и connection которые уже есть в db_connection,
# поэтому просто обращаемся к ним заренее импортировав
cur = db_connection.cursor
conn = db_connection.conn


def insert_data():
    cur.execute(
        "INSERT INTO defective_headset (serial_number, workplace, malfunction) VALUES (%s, %s, %s)",
        (user_text_sn.get(), user_text_rm.get(), breakdown_list.get())
    )

    conn.commit()
    print('Данные записаны')
    conn.close()


root.mainloop()