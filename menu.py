from tabulate import *
from note import Note


class Menu:
    main_Menu = {
        "0": "Главное Меню:",
        "1": "Найти и показать заметку",
        "2": "Добавить заметку",
        "3": "Изменить заметку",
        "4": "Удалить заметку",
        "5": "Просмотр заметок",
        "6": "Импорт/экспорт заметок в файл",
        "10": "Выход"

    }
    notes_exim_Menu = {
        "0": "Сохранение/Загрузка заметок:",
        "1": "Сохранить заметки в Json файл",
        "2": "Загрузить заметки из Json файла",
        "10": "Вернуться в основное меню"
    }

    notes_sort_Menu = {
        "0": "Критерии сортировки заметок:",
        "1": "ID",
        "2": "Название заметки",
        "3": "Время создания",
        "4": "Время изменения",
        "10": "Вернуться в основное меню",
    }

    notes_show_Menu = {
        "0": "Просмотр заметок:",
        "1": "Показать список заметок",
        "2": "Показать все заметки c содержимым",
        "3": "Сортировать заметки",
        "10": "Вернуться в основное меню"
    }

    def show_menu_view(self, obj: dict):
        while True:
            for k, v in obj.items():
                if k == "0":
                    print(v)
                else:
                    print(" ", k, " - ", v)
            choice = input("Выберите пункт: ")
            if choice in obj and choice != "0":
                return choice
            else:
                print("Неправильный ввод. Попробуйте еще раз.")

    def show_note_view(self, obj: Note):
        print(str(obj))

    def note_add_view(self):
        hr = input("Введите заголовок: ")
        txt = ""
        print(
            "Введите заметку. Возможен ввод нескольких строк. Для окончания ввода введите на новой строке цифру 10 и нажмите 'Ввод'")
        while True:
            inp = input()
            if inp == "10":
                break
            txt = txt + inp + "\n"
        return hr, txt

    def list_notes_view(self, objects: list, var=""):
        listnotes = self.conv_to_list(objects, var)
        ncl = Note("", "")
        newheaders = ncl.all_atribs_names()
        # headers = "keys"
        if var == "full":
            width = [3, 20, 70, 10, 10]
        else:
            newheaders.pop(2)
            width = [3, 20, 20, 20]
        if listnotes:
            print(tabulate(listnotes, headers=newheaders, tablefmt="heavy_grid", colalign=("center", "left", "left",),
                           maxcolwidths=width))  # or grid or pretty

    def conv_to_list(self, obj_list, columns="full"):
        newlistlist = []
        if columns == "full":
            for note in obj_list:
                newlistlist.append([note.id, note.header, note.text, note.created, note.last_updated])
        else:
            for note in obj_list:
                newlistlist.append([note.id, note.header, note.created, note.last_updated])
        return newlistlist

    def sort_key(self, obj: Note, argument_key: str):
        index = obj.all_atribs_names().index(argument_key)
        return obj.all_atrib_values()[index]

    def sort_objs_view(self, obj_to_sort):
        while True:
            choice = self.show_menu_view(self.notes_sort_Menu)
            if choice == "10":
                break
            key = self.notes_sort_Menu[choice]
            sort_list = sorted(obj_to_sort, key=lambda note: self.sort_key(note, key))
            self.list_notes_view(sort_list, "full")

    def confirm_msg_view(self):
        print("Операция выполнена успешно!")

    def non_confirm_msg_view(self):
        print("Операция не выполнена")
