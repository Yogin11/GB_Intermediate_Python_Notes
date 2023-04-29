from abc import *
from note import *

class IOoperations(ABC):

    @abstractmethod
    def save(self, file_name: str, data):
        pass

    @abstractmethod
    def load(self, file_name: str):
        return -1

