import datetime

class Note:

    def __init__(self, title: str, text: str):
        self.__id = 0
        self.__header = title
        self.__text = text
        self.__created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__last_updated = self.__created


    def all_atribs_names(self):
        return ["ID", "Название заметки", "Текст заметки", "Время создания", "Время изменения"]

    def all_atrib_values(self):
        return [self.id, self.header, self.text, self.created, self.last_updated]

    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, value):
        self.__created = value

    @property
    def last_updated(self):
        return self.__last_updated

    @last_updated.setter
    def last_updated(self, value):
        self.__last_updated = value

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, value: str):
        self.__header = value
        self.last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value
        self.last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        return f"ID:{self.id} \n Название заметки:  '{self.header}' \n \
Текст заметки:\n\n' {self.text}'\n \
Дата создания: '{self.created}'\n \
Дата изменения: '{self.last_updated}'\n "
