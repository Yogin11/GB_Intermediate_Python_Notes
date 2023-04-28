import os
import platform
import copy
from note import *
import json
from menu import *


class Notebook:
    def __init__(self):
        # self.notes = []
        self.notesobj = []
        self.n = 0
        self.menu = Menu()
        self.import_notes()

    def start(self):
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

        input("↩")
        self.start()

    def notes_show(self):
        choice = self.menu.show_menu_view(self.menu.notes_show_Menu)
        self.clr_scr()
        match choice:
            case "1":
                self.show_notes_brief(self.dict_convert(self.notesobj))
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
        self.notes_show()

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
        self.note_actions()

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

    def show_notes_full(self):
        self.menu.list_notes_view(self.dict_convert(self.notesobj), "full")

    def show_notes_brief(self, notes_list):
        newnoteslist = copy.deepcopy(notes_list)
        for k in newnoteslist:
            del k["Текст заметки:"]
        self.menu.list_notes_view(newnoteslist)

    def show_note(self):
        found_list_obj = self.search_context()
        self.menu.show_note_view(found_list_obj)

    def add_note(self):
        self.n += 1
        hr, txt = self.menu.note_add_view()
        obj = Note(hr, txt)
        obj.id = self.n
        self.notesobj.append(obj)
        self.menu.confirm_msg_view()

    def sort_key(self, obj: dict, argument_key: str):
        return obj[argument_key]

    def sort_objs(self):
        while True:
            choice = self.menu.show_menu_view(self.menu.notes_sort_Menu)
            if choice == "10":
                break
            key = self.menu.notes_sort_Menu[choice] + ":"
            sort_list = sorted(self.dict_convert(self.notesobj), key=lambda note: self.sort_key(note, key))
            self.menu.list_notes_view(sort_list, "full")

    def save_notes(self):
        newlist = []
        with open("notes11.json", "w", encoding='utf8') as file:
            for obj in self.notesobj:
                somevar = json.dumps(obj, cls=self.Encoder, ensure_ascii=False, indent=3)
                someloadsobj = json.loads(somevar)
                newlist.append(someloadsobj)
            json.dump(newlist, file, ensure_ascii=False, indent=3)
        self.menu.confirm_msg_view()

    class Encoder(json.JSONEncoder):
        def default(self, nt):
            return {"ID:": nt.id,
                    "Название заметки:": nt.header,
                    "Текст заметки:": nt.text,
                    "Время создания:": nt.created,
                    "Время изменения:": nt.last_updated,
                    }

    def import_notes(self):
        self.note_objs = []
        # self.notes = []
        with open("notes11.json", "r", encoding='utf8') as file:
            data = json.load(file)
            self.n = 0
            for i in data:
                nt = Note("", "")
                nt.id = i["ID:"]
                nt.header = i["Название заметки:"]
                nt.text = i["Текст заметки:"]
                nt.created = i["Время создания:"]
                nt.last_updated = i["Время изменения:"]
                self.notesobj.append(nt)
                # self.notes.append(i)
            self.n = self.notesobj[-1].id
        self.menu.confirm_msg_view()

    def dict_convert(self, obj_list):
        new_dict_list = []
        dict_note = {}
        for note in obj_list:
            dict_note["ID:"] = note.id
            dict_note["Название заметки:"] = note.header
            dict_note["Текст заметки:"] = note.text
            dict_note["Время создания:"] = note.created
            dict_note["Время изменения:"] = note.last_updated
            new_dict_list.append(dict_note)
            dict_note = {}
        return new_dict_list

    def edit_note(self):
        note = self.choose_from_foundlist("для редактирования: ")
        if note:
            new_header = input("Введите новый заголовок заметки. Чтобы заголовок оставить прежним, нажмите 'Enter'. \n>")
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

    def search_context(self):
        note_substring = input("Введите первые буквы заголовка заметки: ")
        match = -1
        found_list_obj = []
        for note in self.notesobj:
            match = note.header.lower().find(note_substring.lower())
            if match != -1:
                found_list_obj.append(note)
        if found_list_obj:
            print(f"Найдено записей {len(found_list_obj)} ")
            self.show_notes_brief(self.dict_convert(found_list_obj))
            return found_list_obj
        else:
            print("Заметка не найдена")
            return ""

    def choose_from_foundlist(self, call=""):
        found_list_obj = self.search_context()
        if found_list_obj:
            note = ""
            if len(found_list_obj) == 1:
                note = found_list_obj[0]
            else:
                id_input = input("Введите ID заметки " + call)
                for item in found_list_obj:
                    if item.id == int(id_input):
                        print()
                        print("Текущая заметка: ")
                        print()
                        note = item
                        break
                if not note:
                    print("Неверный ввод")
            self.menu.show_note_view(note)
            return note

    def delete_note(self):
        note = self.choose_from_foundlist("для удаления: ")
        if note:
            confirm = input("!!! Подтвердите удаление 1- да, 2 - нет")
            if confirm == "1":
                self.notesobj.remove(note)
                self.menu.confirm_msg_view()
            else:
                self.menu.non_confirm_msg_view()
