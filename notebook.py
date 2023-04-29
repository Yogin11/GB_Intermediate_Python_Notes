import os
import platform
from menu import *
from opsjson import *
from search import *


class Notebook:

    def __init__(self):
        self.notes_obj = []
        self.n = 0
        self.menu = Menu()
        self.filename = "notes11.json"
        self.import_notes()

    def start(self):
        choice = self.menu.show_menu_view(self.menu.main_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.menu.show_note_view(Search().choose_from_foundlist(self.notes_obj))
            case "2":
                self.add_note()
            case "3":
                self.edit_note()
            case "4":
                self.delete_note()
            case "5":
                self.notes_show()
            case "6":
                self.notes_exim()

            case "10":
                exit()
        input("↩")
        self.clr_scr()
        self.start()

    def notes_show(self):
        choice = self.menu.show_menu_view(self.menu.notes_show_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.menu.list_notes_view(self.notes_obj)
            case "2":
                self.menu.list_notes_view(self.notes_obj, "full")
            case "3":
                self.menu.sort_objs_view(self.notes_obj)
            case "10":
                self.start()
        input("↩")
        self.clr_scr()
        self.notes_show()

    def notes_exim(self):
        choice = self.menu.show_menu_view(self.menu.notes_exim_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.save_notes()
            case "2":
                self.import_notes()
            case "10":
                self.start()
        input("↩")
        self.clr_scr()
        self.notes_exim()

    def clr_scr(self):
        system_name = platform.system()
        if system_name == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def add_note(self):
        self.n += 1
        hr, txt = self.menu.note_add_view()
        obj = Note(hr, txt)
        obj.id = self.n
        self.notes_obj.append(obj)
        self.menu.confirm_msg_view()

    def save_notes(self):

        fname = input(f"Введите имя файла с расширением .json. По умолчанию данные сохранятся в '{self.filename}' >")
        match = fname.find(".json")
        if (not fname) or (match == -1):
            fname = self.filename
        else:
            self.filename = fname
        JsonIO().save(fname, self.notes_obj)
        self.menu.confirm_msg_view()

    def import_notes(self):
        print()
        fname = input(
            f"Введите имя Json файла, находящегося в папке проекта. Нажмите ввод для загрузки по умолчанию из файла'{self.filename}' >")
        if not fname:
            fname = self.filename
        if os.path.exists(fname):
            self.n, self.notes_obj = JsonIO().load(fname)
            if self.n != 0:
                self.filename = fname
                self.menu.confirm_msg_view()
            else:
                print("Неверный формат Json данных для данной программы")
                self.import_notes()
        else:
            self.menu.non_confirm_msg_view()
            print("Попробуйте еще раз")
            self.import_notes()

    def edit_note(self):
        note = Search().choose_from_foundlist(self.notes_obj, "для редактирования: ")
        self.menu.show_note_view(note)
        if note:
            new_header = input(
                "Введите новый заголовок заметки. Чтобы заголовок оставить прежним, нажмите 'Enter'. \n>")
            if new_header:
                note.header = new_header
            choice = input("Если нужно текст оставить прежним, нажмите 'Enter' \ "
                           "Чnобы добавить текст к существующей заметке нажмите 1, заменить текст 2. Для окончания ввода наберите 10 на новой строке \n>")
            new_text = ""
            if choice == "1":
                new_text = note.text + " "
            while True:
                inp = input(">")
                if inp == "10" or inp == "":
                    break
                new_text = new_text + inp + "\n"
            if new_text:
                note.text = new_text
            print(f"Заметка успешно отредактирована!")

    def delete_note(self):
        note = Search().choose_from_foundlist(self.notes_obj, "для удаления: ")
        self.menu.show_note_view(note)
        if note:
            confirm = input("!!! Подтвердите удаление 1- да, 2 - нет")
            if confirm == "1":
                self.notes_obj.remove(note)
                self.menu.confirm_msg_view()
            else:
                self.menu.non_confirm_msg_view()
