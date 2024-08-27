from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("Process is running in Laptop")


class Desktop(Computer):

    def process(self):
        print("Process is running in Desktop")


lap = Laptop()
desk = Desktop()
lap.process()
desk.process()
