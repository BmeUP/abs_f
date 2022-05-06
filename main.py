from src.abstract_classes import GUIFactory, Button, Checkbox
from src.win.ui_factory import WinFactory
from src.mac.ui_factory import MacFactory


class Application(object):
    def __init__(self, factory) -> None:
        self.factory: GUIFactory = factory()
        self.button: Button = None
        self.checkbox: Checkbox = None
    
    def create_ui(self):
        self.button = self.factory.create_btn()
    
    def paint(self):
        self.button.paint()


win_ui = Application(WinFactory)
mac_ui = Application(MacFactory)