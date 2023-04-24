from hmac import new
from re import Pattern
import re
from note import *
import json

class Notebook:
    
    def __init__(self):
        self.notes=[]
        self.n = 0
        
    def add_note(self):
        self.n += 1
        hr = input("Введите заголовок: ")
        txt=""
        print("Введите заметку. Возможен ввод нескольких строк. Для окончания ввода введите на новой строке цифру 10 и нажмите 'Ввод'") 
        while True:
            inp = input()
            if inp=="10":
                break
            txt = txt +  inp + "\n"
        self.notes.append((self.n, str(Note(hr,txt))))
        print("Note added successfully!")
       
    def show_notes(self):
        for note in self.notes:
            print(f" Заметка №{note[0]} \n {note[1]}")
            
            
    def __str__(self):
        return self.notes
    
    def import_notes(self):
        pass
    
    def save_notes(self):
        with open("notes1.json", "w", encoding='utf8') as file:
            json.dump(self.notes, file,ensure_ascii=False, indent=3)
        print("Notes saved successfully!")
    
    def import_notes(self):
        self.notes = []
        with open("notes1.json", "r",encoding='utf8' ) as file:
            self.notes = json.load(file)
        print("Notes imported successfully!")

    def edit_note(self):
        note_number = input("Введите первые буквы названия заметки, которую нужно редактировать: ")
        
        ### поиск заметки
        note1 = Note("testname","test content")
        if not note1: 
            print(f"Заметка не найдена")       
        else:
            print(f"Текущая заметка: {note1}")
            new_header = input("Введите новый заголовок заметки. Если заголовок оставить прежним, нажмите 'Enter'")
            if new_header:
                note1.header(new_header)
            new_text = input("Введите новый текст заметки. Если нужно текст оставить прежним, нажмите 'Enter'")
                ## Доработать возможность редактировать заметку в текст редакторе или еще как-то
            if new_text:
                note1.text(new_text)   
            print(f"Заметка успешно отредактирована!")
        
    def search_context():
        # pattern =r'\+?[0-9]{11}$'
        # while True:                 
        #     check=input("Введите телефон нового контакта (не более 11 цифр): ")
        #     if re.match(Pattern,check):
        #         # newadd.append(check)   
        #         break
        #     else:
        #         print("Некорретный ввод, попробуйте еще раз")
        pass

