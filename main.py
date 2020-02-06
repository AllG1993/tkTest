from tkinter import *
from tkinter.ttk import Combobox
import db_connection

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
    result_user_data()
    insert_data()


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


def result_user_data():
    get_user_text_sn = user_text_sn.get()
    get_user_text_rm = user_text_rm.get()
    get_breakdown_list = breakdown_list.get()
    get_user_data_collection = (get_user_text_sn, get_user_text_rm, get_breakdown_list)
    print(get_user_data_collection)


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


window.mainloop()