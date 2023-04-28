from tabulate import *

# from note import Note

class Menu:
    main_Menu = {
        "0": "Главное Меню:",
        "1": "Просмотр заметок: показать, сортировать",
        "2": "Действия с заметками: Добавить, изменить, удалить",
        "3": "Импорт/экспорт заметок в файл",
        "10": "Выход"
    }
    notes_sort_Menu = {
        "0": "Критерии сортировки заметок:",
        "1": "ID",
        "2": "Название заметки",
        "3": "Время создания",
        "4": "Время изменения",
        "10": "Вернуться в меню 'Действия с заметками'",
    }

    notes_show_Menu = {
        "0": "Просмотр заметок:",
        "1": "Показать список заметок",
        "2": "Показать все заметки c содержимым",
        "3": "Сортировать заметки",
        "4": "Найти и показать заметку",
        "10": "Вернуться в основное меню"
    }
    notes_action_Menu = {
        "0": "Действия с заметками:",
        "1": "Добавить заметку",
        "2": "Изменить заметку",
        "3": "Удалить заметку",
        "10": "Вернуться в основное меню"

    }
    notes_exim_Menu = {
        "0": "Сохранение/Загрузка заметок:",
        "1": "Сохранить заметки в Json файл",
        "2": "Загрузить заметки из Json файла",
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

    def show_note_view(self, obj_list):
        if isinstance(obj_list, list):
            note = obj_list[0]
            if len(obj_list) > 1:
                choice = input("Выберите ID заметки: ")
                for obj in obj_list:
                    if obj.id == choice:
                        note = obj
                        break
        else:
            note = obj_list
        print(str(note))

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

    def list_notes_view(self, listnotes: list, var=""):

        if var == "full":
            width = [3, None, None, 10, 10]
        else:
            width = [3, None, 10, 10]
        if listnotes:
            print(tabulate(listnotes, headers="keys", tablefmt="heavy_grid", colalign=("center","left","left",),
                           maxcolwidths=width))  # or grid or pretty

    def confirm_msg_view(self):
        print("Операция выполнена успешно!")

    def non_confirm_msg_view(self):
        print("Операция не выполнена")
