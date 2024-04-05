from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def tvManufacture(self):
       pass

    def tvRepaire(self):
        print("Tv repaire")