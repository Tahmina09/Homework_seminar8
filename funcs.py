import csv
import view as v

def export_data():
    data = []
    choice = v.choose_format()
    
    if choice == '1':
        with open('telephone_book.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            list_cont = data.split("\n\n")
        return list_cont
    elif choice == '2':
        with open('telephone_book.csv', 'r', encoding='utf-8') as file:
            for line in file:
                if ';' in line:
                    temp = line.strip().split(';')
                    data.append(temp)
        return data
    else:
        print('Некорректный ввод! Попробуйте ещё раз!')

def import_book():
    choice = v.choose_format()
    name = input('Введите имя файла, из которого импортируется телефонная книга - ')
    with open (f'{name}.txt', 'r', encoding='UTF - 8') as f:
        im_data = f.read()
    if choice == '1':
        with open('telephone_book.txt', 'a', encoding='UTF - 8'):
            f.write(im_data + '\n\n')
    elif choice == '2':
        with open ('telephone_book.csv', 'r', encoding='UTF - 8') as f:
            read = csv.reader(f)
            for row in read:
                    with open('telephone.csv', 'a', encoding='UTF - 8', newline='\n') as f:
                        write = csv.writer(f)
                        write.writerow(row)
    else:
        print('Некорректный ввод! Попробуйте ещё раз!')
            


def add_contact():
    choice = v.choose_format()
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    telephone = input('Введите телефон: ') 
    if choice == '1':   
        with open('telephone_book.txt', 'a', encoding= 'UTF - 8') as data:
            data.write(f'\n\n{surname} \n{name} \n{telephone}')
    elif choice == '2':
        with open('telephone_book.csv', 'a', newline='', encoding=' UTF - 8') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\r')
            writer.writerow([f'{name}; {surname}; {telephone}'])    
    else:
        print('Некорректный ввод! Попробуйте ещё раз!')
        
        
def search_data():
    data = export_data()
    choice = v.choose_format()
    data_list = []
    val = 1
    word = input('Введите имя или фамилию -> ')
    if choice == '1':
        for line in data:
            if word in line:
                val = 0
                data_list.append(line)
    elif choice == '2':
        for line in data:
            for i in line:
                if word in i:
                    val = 0
                    data_list.append(line)
    else:
        print('Некорректный ввод! Попробуйте ещё раз!')
        
            
    if val: print('Такого контакта нет!')
    return data_list