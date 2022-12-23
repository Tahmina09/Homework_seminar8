import tkinter as tk
import funcs as f

def menu():
    win = tk.Tk()
    win.title("Phone Book")
    win.geometry("500x400+40+40")

    lable_1 = tk.Label(win, text="Здравствуйте!\nВас приветствует самая лучшая телефонная книга",
                       fg="black",
                       )
    lable_1.pack()

    but_1 = tk.Button(win, text="Добавить контакт",
                     activebackground="violet",
                     width=32,
                     height=2
                     )

    but_2 = tk.Button(win, text="Поиск контакта",
                     activebackground="violet",
                     width=32,
                     height=2
                     )

    but_3 = tk.Button(win, text="Импорт телефонной книги",
                     activebackground="violet",
                     width=32,
                     height=2
                     )

    but_4 = tk.Button(win, text="Экспорт телефонной книги",
                     activebackground="violet",
                     width=32,
                     height=2
                     )


    but_1.pack()
    but_2.pack()
    but_3.pack()
    but_4.pack()

    win.mainloop()
    
menu()


def choose_format():
    form = input('В каком формате хотите сохранить данные:\
        \n выберите 1 - в формате .txt;\
            \n выберите 2 - в формате .csv;\
                \n Ваш выбор: ')
    return form