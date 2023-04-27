# from re import Pattern
# import re
import os
import platform
import copy

from note import *
import json
from menu import *


class Notebook:
    dict = {}

    def __init__(self):
        self.notes = []
        self.notesobj = []
        self.n = 0
        self.menu = Menu()
        self.dict = {"notebook": self.notes}
        self.import_notes()

    def start(self):
        # self.import_notes()
        choice = self.menu.show_menu_view(self.menu.main_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.notes_show()
            case "2":
                self.note_actions()
            case "3":
                self.notes_exim()
            case "10":
                exit()

        self.start()
        input("↩")
        # self.clr_scr()

    def notes_show(self):
        choice = self.menu.show_menu_view(self.menu.notes_show_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.show_notes_brief(self.notes)
            case "2":
                self.show_notes_full()
            case "3":
                self.sort_objs()
            case "4":
                self.show_note()
            case "10":
                self.start()

        input("↩")
        self.clr_scr()

    def note_actions(self):
        choice = self.menu.show_menu_view(self.menu.notes_action_Menu)
        self.clr_scr()

        match choice:
            case "1":
                self.add_note()
            case "2":
                self.edit_note()
            case "3":
                self.delete_note()
            case "10":
                self.start()
        input("↩")
        self.clr_scr()

    def notes_exim(self):
        choice = self.menu.show_menu_view(self.menu.notes_exim_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.save_notes()
            case "2":
                self.import_notes()
        input("↩")
        self.clr_scr()

    def clr_scr(self):
        system_name = platform.system()
        if system_name == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def show_notes_full(self):
        width = [3, None, None, 10, 10]
        self.menu.list_notes_view(self.notes, width)

    def show_notes_brief(self, notes_list):
        newnoteslist = copy.deepcopy(notes_list)
        for k in newnoteslist:
            del k["Текст заметки:"]
        self.menu.list_notes_view(newnoteslist)

    def show_note(self):
        found_list_dict, found_list_obj = self.search_context()
        self.menu.show_note_view(found_list_obj)

    def add_note(self):
        self.n += 1
        hr, txt = self.menu.note_add_view()
        # self.notes.append((self.n, str(Note(hr, txt))))
        obj = Note(hr, txt)
        obj.id = self.n
        y = json.dumps(obj, cls=self.TestEncoder, ensure_ascii=False, indent=2)
        i = json.loads(y)
        self.notes.append(i)
        self.notesobj.append(obj)
        self.dict["notebook"] = self.notes
        self.menu.confirm_msg_view()

    def sort_key(self, obj: dict, argument_key: str):
        return obj[argument_key]

    def sort_objs(self):
        while True:
            # choice = self.menu.show_sort_choice_view()
            choice = self.menu.show_menu_view(self.menu.notes_sort_Menu)
            # if choice == "10": break
            key = self.menu.notes_sort_Menu[choice] + ":"
            sort_list = sorted(self.notes, key=lambda note: self.sort_key(note, key))
            self.menu.list_notes_view(sort_list)

    def save_notes(self):
        newlist = []

        with open("notes11.json", "w", encoding='utf8') as file:
            for obj in self.notesobj:
                somevar = json.dumps(obj, cls=self.TestEncoder, ensure_ascii=False, indent=2)
                print("try save from dumps - ", somevar)
                newlist.append(somevar)
            self.dict["notebook"] = newlist
            json.dump(self.dict, file, ensure_ascii=False, indent=2)
        self.menu.confirm_msg_view()

    class TestEncoder(json.JSONEncoder):
        def default(self, nt):
            return {"ID:": nt.id,
                    "Название заметки:": nt.header,
                    "Текст заметки:": nt.text,
                    "Время создания:": nt.created,
                    "Время изменения:": nt.last_updated,
                    }

    def import_notes(self):
        self.note_objs = []
        self.notes = []
        with open("notes11.json", "r", encoding='utf8') as file:
            data = json.load(file)
            # y = json.loads()
            self.n = 0
            for i in data['notebook']:
                self.n += 1
                y = json.loads(i)
                nt = Note("", "")
                nt.id = y["ID:"]
                nt.header = y["Название заметки:"]
                nt.text = y["Текст заметки:"]
                nt.created = y["Время создания:"]
                nt.last_updated = y["Время изменения:"]
                self.notesobj.append(nt)
                self.notes.append(y)
        self.menu.confirm_msg_view()

        # note_substring = input("Выберите ID заметки для просмотра: ")

    def edit_note(self):
        # note_substring = input("Введите первые буквы заголовка заметки, которую нужно редактировать: ")
        found_list_dict, found_list_obj = self.search_context()
        if found_list_dict:
            note = ""
            if len(found_list_obj) == 1:
                note = found_list_obj[0]

            else:
                id_input = input("Введите ID заметки для редактирования: ")
                # for note_dict in found_list_dict:
                for item in found_list_obj:
                    # if note_dict.get("ID:") == int(id_input):
                    if item.id == int(id_input):
                        print("Текущая заметка: ")
                        width = [3, None, None, 10, 10]
                        note = item
                        break
                    # self.menu.list_notes_view(list(note_dict), width)
            index = self.notesobj.index(note)

            self.menu.show_note_view(note)
            new_header = input("Введите новый заголовок заметки. Чтобы заголовок оставить прежним, нажмите 'Enter'")
            if new_header:
                self.notes[index]["Название заметки"] = new_header
                note.header = new_header

            print("Введите новый текст заметки. Если нужно текст оставить прежним, нажмите 'Enter'. \
            Для окончания ввода наберите 10 на новой строке")
            new_text = ""
            while True:
                inp = input()
                if inp == "10" or inp == "":
                    break
                new_text = new_text + inp + "\n"
            if new_text:
                self.notes[index]["Текст заметки:"] = new_text
                note.text = new_text
            print(f"Заметка успешно отредактирована!")

    def search_context(self):
        note_substring = input("Введите первые буквы заголовка заметки: ")
        match = -1
        k = 0
        found_list = []
        found_list_obj = []
        for item in self.notes:
            note_obj = self.notesobj[self.notes.index(item)]
            poisk = item["Название заметки:"].lower()
            match = poisk.find(note_substring.lower())
            if match != -1:
                k += 1
                found_list.append(item)
                found_list_obj.append(note_obj)
                # print("FOUND!!! ", k)
                # width = [3, None, None, 10, 10]
                # self.menu.list_notes_view(found_list, width)
        if found_list:
            print(f"Найдено записей {len(found_list)} ")
            # width = [3, None, None, 10, 10]
            self.show_notes_brief(found_list)  # , width)
            return found_list, found_list_obj
        else:
            print("Строка не найдена")
            return "", ""

    def delete_note(self):

        pass
