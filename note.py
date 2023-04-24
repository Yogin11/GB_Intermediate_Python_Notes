import datetime


class Note:
    
    def __init__(self, header: str, text: str):
        self.header = header
        self.text = text
        self.created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.lastupdated = self.created
    
    @property
    def header(self):
        return self.header
    
    @header.setter
    def header(self, value: str):
        self.header = value
        self.lastupdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    @property
    def text(self):
        return self.text
    
    @text.setter
    def text(self, value: str):
        self.text = value  
        self.lastupdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        
    def __str__(self):
        return f"Название заметки:{self.header} \n\
Текст заметки: \n{self.text}\n\
Дата создания: {self.created}\n\
Дата изменения: {self.lastupdated}\n"
    

 
    
            

