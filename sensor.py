from abc import ABC, abstractmethod

class Sensor(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def query(self):
        pass
    