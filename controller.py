import view as v
import funcs as f 

def phone_button():
    menu_item = v.menu()
    if menu_item == but_1:
        f.add_contact()
    elif menu_item == but_2:
        f.search_data()
    elif menu_item == but_3:
        f.import_book()
    elif menu_item == but_4:
        f.export_data()
    else:
        print('Такой команды не обнаружено. Попробуйте ещё раз!')