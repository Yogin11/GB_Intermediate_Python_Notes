# from re import Pattern
# import re
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

    def start(self):
        # self.import_notes()
        while True:
            choice = self.menu.show_menu_view()
            match choice:
                case "1":
                    self.show_notes()
                case "2":
                    self.add_note()
                case "3":
                    self.edit_note()
                case "4":
                    self.delete_note()
                case "5":
                    self.save_notes()
                case "6":
                    self.import_notes()
                case "10":
                    break

    def show_notes(self):
        self.menu.list_notes_view(self.notes)

    def add_note(self):
        self.n += 1
        hr, txt = self.menu.note_add_view()
        # self.notes.append((self.n, str(Note(hr, txt))))
        obj = Note(hr, txt)
       
        y = json.dumps(obj, cls=self.TestEncoder,ensure_ascii=False, indent=2)
        i = json.loads(y)
        self.notes.append(i)
        self.notesobj.append(obj)
        self.dict["notebook"] = self.notes

        self.menu.confirm_msg_view()

    def save_notes(self):
        newlist = []

        with open("notes11.json", "w", encoding='utf8') as file:
            # json.dump(self.notes, file, ensure_ascii=False, indent=3)
            # ser_obj = json.dumps(self.dict,default=lambda x: x.__dict__,ensure_ascii=False, indent=2 )
            for obj in self.notesobj:
                somevar = json.dumps(obj, cls=self.TestEncoder,ensure_ascii=False, indent=2)
                print("try save from dumps - ", somevar)
                newlist.append(somevar)
            self.dict["notebook"] = newlist
            json.dump(self.dict, file, ensure_ascii=False, indent=2)
        self.menu.confirm_msg_view()

    class TestEncoder(json.JSONEncoder):
        def default(self, nt):
            return {"Название заметки:": nt.header,
                    "Текст заметки:": nt.text,
                    "Дата создания:": nt.created,
                    "Дата изменения:": nt.last_updated,
                    }

    def import_notes(self):
        self.note_objs = []
        self.notes = []
        with open("notes2.json", "r", encoding='utf8') as file:
            data = json.load(file)
            # y = json.loads()
            for i in data['notebook']:
                y = json.loads(i)
                print ("type y = ", type(y))
                nt = Note("","")
                nt.header = y["Название заметки:"]
                nt.text = y["Текст заметки:"]
                nt.created = y["Дата создания:"]
                nt.last_updated = y["Дата изменения:"]
                self.notesobj.append(nt)
                self.notes.append(y)
        self.menu.confirm_msg_view()


    def edit_note(self):
        note_substring = input("Введите первые буквы заголовка заметки, которую нужно редактировать: ")
        match = -1
        n = 0
        foundlist = []
        for item in self.notes:
            poisk = item["Название заметки:"].lower()
            # poisk = item.header.lower()
            # print(poisk)
            # print(note_substring)
            match = poisk.find(note_substring.lower())
            if match != -1:
                n+=1
                foundlist.append(item)
                print("FOUND!!! ", n)
                # print(note)
               
        self.menu.list_notes_view(foundlist)
        # if match != -1:
        #     print("Not found")
        # else:
        #     print("FOUND!!!")

        ### поиск заметки

        # if match == -1:
        #     print(f"Заметка не найдена")
        # else:
        #     print(f"Текущая заметка: {found_note}")
        #     new_header = input("Введите новый заголовок заметки. Если заголовок оставить прежним, нажмите 'Enter'")
        #     if new_header:
        #         note1.header(new_header)
        #     new_text = input("Введите новый текст заметки. Если нужно текст оставить прежним, нажмите 'Enter'")
        #     ## Доработать возможность редактировать заметку в текст редакторе или еще как-то
        #     if new_text:
        #         note1.text(new_text)
        #     print(f"Заметка успешно отредактирована!")

    def search_context(self):
        # pattern =r'\+?[0-9]{11}$'
        # while True:                 
        #     check=input("Введите телефон нового контакта (не более 11 цифр): ")
        #     if re.match(Pattern,check):
        #         # newadd.append(check)   
        #         break
        #     else:
        #         print("Некорретный ввод, попробуйте еще раз")
        pass

    def delete_note(self):
        
        pass
