import datetime


class Note:
    # note = {}

    def __init__(self, title: str, text: str):
        self.__header = title
        self.__text = text
        self.__created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__last_updated = self.created
        self.__note = {"Название заметки:": self.__header,
                     "Текст заметки:": self.__text,
                     "Дата создания:": self.__created,
                     "Дата изменения:": self.__last_updated
                     }

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

    @property
    def note(self):
        return self.__note


    def __str__(self):
        return str(self.note)
#         return f"Название заметки:{self.header} \n\
# Текст заметки: \n{self.text}\n\
# Дата создания: {self.created}\n\
# Дата изменения: {self.last_updated}\n"
