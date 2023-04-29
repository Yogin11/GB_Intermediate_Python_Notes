from menu import *


class Search:

    def search_context(self, data):
        note_substring = input("Введите набор символов для поиска в заголовках и текстах заметок: ")
        match1 = -1
        match2 = -1
        found_list_obj = []
        for note in data:

            match1 = note.header.lower().find(note_substring.lower())
            match2 = note.text.lower().find(note_substring.lower())

            if match1 != -1 or match2 != -1:
                found_list_obj.append(note)
        return found_list_obj

    def choose_from_foundlist(self, data, call="", ):
        found_list_obj = self.search_context(data)
        if found_list_obj:
            print(f"Найдено записей {len(found_list_obj)} ")
            Menu().list_notes_view(found_list_obj, "notfull")
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
            return note
        else:
            print("Заметка не найдена")
            return ""
