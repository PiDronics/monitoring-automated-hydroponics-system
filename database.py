from abc import ABC, abstractmethod

class Database(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def push(self):
        pass
    
    @abstractmethod
    def authenticate(self):
        pass