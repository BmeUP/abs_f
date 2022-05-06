from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        ...


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        ...


class GUIFactory(ABC):
    @abstractmethod
    def create_btn(self):
        ...
    
    @abstractmethod
    def create_checkbox(self):
        ...