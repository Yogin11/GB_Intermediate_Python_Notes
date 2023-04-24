class Menu:
    mainMenu  = {
        "1": "Show all notes",
        "2": "Add note",
        "3": "Edit note",
        "4": "Delete note",    
        "5": "Save notes",
        "6": "Import notes",
        "10": "Exit"
        }
    def show_menu(self):
        for f in self.mainMenu:
            print(f, self.mainMenu[f])
        choice = input("Enter your choice: ")
        
        
        return choice