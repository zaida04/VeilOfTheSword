from abc import ABC, abstractmethod

class Armour(ABC):
    @abstractmethod
    def resist(self):
        pass
