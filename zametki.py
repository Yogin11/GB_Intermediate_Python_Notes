import json
import datetime
from operator import indexOf
from os import system
notes = []
system('cls')

def show_notes():
    if not notes:
        print("There are no notes yet!")
    else:
        for note in notes:
            print("Номер заметки: {}".format(indexOf(notes,note)+1))
            print("header: {}".format(note["header"]))
            print("Text: {}".format(note["text"]))
            print("Created: {}".format(note["created"]))
            print("Last modified: {}".format(note["last_modified"]))
            # print("Author: {}".format(note["author"]))
            print("")
def add_note():
    header = input("Enter header: ")
    text = input("Enter text: ")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_modified = created
    # author = input("Enter author: ")
    note = {
        "header": header,
        "text": text,
        "created": created,
        "last_modified": last_modified,
        # "author": author
    }
    notes.append(note)
    print("Note added successfully!")
def edit_note():
    
     # Запросить у пользователя номер заметки, которую нужно редактировать
    note_number = int(input("Введите номер заметки, которую нужно редактировать: "))
    # print (note_number)
    # print (notes[1])
    # for note in notes:
    #     print(note)
    note_number-=1
    if notes[note_number]:
      
        print(f"Текущая заметка: {notes[note_number]}")
        new_text = input("Введите новый текст заметки: ")
        notes[note_number]["text"] = new_text
        notes[note_number]["last_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Заметка номер {note_number+1} успешно отредактирована!")
    else:
        print(f"Заметки с номером {note_number} не существует.")
    
    ###
    # header = input("Enter header of the note you want to edit: ")
    # for note in notes:
    #     if note["header"] == header:
    #         text = input("Enter new text: ")
    #         note["text"] = text
    #         note["last_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #         print("Note edited successfully!")
    #         return
    # print("Note not found!")
    ##
def delete_note():
    header = input("Enter header of the note you want to delete: ")
    for note in notes:
        if note["header"] == header:
            notes.remove(note)
            print("Note deleted successfully!")
            return
    print("Note not found!")
def save_notes():
    with open("notes.json", "w", encoding='utf8') as file:
        json.dump(notes, file,ensure_ascii=False, indent=(""))
    print("Notes saved successfully!")
def import_notes():
    global notes
    with open("notes.json", "r") as file:
        notes = json.load(file)
    print("Notes imported successfully!")
    
    
while True:
    print("Menu:")
    print("1. Show notes")
    print("2. Add note")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Save notes")
    print("6. Import notes")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        show_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        save_notes()
    elif choice == "6":
        import_notes()
    elif choice == "7":
        break
    else:
        print("Invalid choice, please try again!")
        
    
    