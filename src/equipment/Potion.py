from abc import ABC, abstractmethod

class Potion(ABC):
    @abstractmethod
    def effect(self):
        pass
