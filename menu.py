from tabulate import *

from note import Note

class Menu:
    mainMenu = {
        "1": "Показать все заметки",
        "2": "Добавить заметку",
        "3": "Изменить заметку",
        "4": "Удалить заметку",
        "5": "Сохранить заметки в файл",
        "6": "Загрузить заметки из файла",
        "10": "Выход"
    }

    def show_menu_view(self):
        for f in self.mainMenu:
            print(f, self.mainMenu[f])
        choice = input("Enter your choice: ")
        if choice in self.mainMenu:
            return choice
        else:
            print("Неправильный ввод. Попробуйте еще раз.")

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
    # def convert_set(set): 
    #      return [*set, ] 
     
    def list_notes_view(self, listnotes: list):
        n=0
        # print ("strnotes = ",[*listnotes[0].note.keys()])
        # lst = [*listnotes[0].note.keys()]
        if listnotes:
            print(tabulate(listnotes,headers="keys", tablefmt="grid", colalign=("left"),stralign='left', maxcolwidths=[None,None, 12,12]))  # or grid or pretty              

    def confirm_msg_view(self):
        print("Операция выполнена успешно!")
