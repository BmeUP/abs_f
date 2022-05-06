from ..abstract_classes import GUIFactory
from .ui_elements import WinButton, WinCheckbox


class WinFactory(GUIFactory):
    def create_btn(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()