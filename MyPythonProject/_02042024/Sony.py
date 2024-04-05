from _02042024.Abstraction import Agent
from _02042024.LaptopAgent import LaptopAgent


class Sony(Agent,LaptopAgent):
    def tvManufacture(self):
        print("TV manufacture...")

    def laptopManufacture(self):
        print("Laptop Manufacture")

    def mobileManufacture(self):
        print("Mobile manufactrue")