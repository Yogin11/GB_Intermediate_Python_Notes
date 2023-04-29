from ioopers import *
import json
from json import JSONDecodeError


class JsonIO(IOoperations):

    def save(self, file_name: str, data):
        new_list = []
        with open(file_name, "w", encoding='utf8') as file:
            for obj in data:
                str_line = json.dumps(obj, cls=self.Encoder, ensure_ascii=False, indent=3)
                new_list.append(json.loads(str_line))
            json.dump(new_list, file, ensure_ascii=False, indent=3)

    class Encoder(json.JSONEncoder):
        def default(self, nt):
            return {"ID:": nt.id,
                    "Название заметки:": nt.header,
                    "Текст заметки:": nt.text,
                    "Время создания:": nt.created,
                    "Время изменения:": nt.last_updated,
                    }

    def load(self, file_name: str):
        notesobj = []
        try:
            with open(file_name, "r", encoding='utf8') as file:
                data = json.load(file)
                for i in data:
                    nt = Note("", "")
                    nt.id = i["ID:"]
                    nt.header = i["Название заметки:"]
                    nt.text = i["Текст заметки:"]
                    nt.created = i["Время создания:"]
                    nt.last_updated = i["Время изменения:"]
                    notesobj.append(nt)
                n = notesobj[-1].id
        except JSONDecodeError:
            n = 0
            notesobj = []
        return n, notesobj
