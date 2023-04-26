class Menu:
    mainMenu = {
        "1": "Show all notes",
        "2": "Add note",
        "3": "Edit note",
        "4": "Delete note",
        "5": "Save notes",
        "6": "Import notes",
        "10": "Exit"
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

    def list_notes_view(self, listnotes: list):
        n=0
        for note in listnotes:
            n+=1
            # print(f" Заметка №{n} \n {note}")
            print(f" Заметка №{n} \n")
            for k in note:
                print(k,note[k])

    def confirm_msg_view(self):
        print("Операция выполнена успешно!")
