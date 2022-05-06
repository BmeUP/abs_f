from ..abstract_classes import GUIFactory
from .ui_elements import MacButton, MacCheckbox


class MacFactory(GUIFactory):
    def create_btn(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()