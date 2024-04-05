from abc import ABC, abstractmethod


class LaptopAgent(ABC):
    @abstractmethod
    def laptopManufacture(self):
        pass

    def laptopRepaire(self):
        print("Laptop repaire")
