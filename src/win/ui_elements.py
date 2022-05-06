from ..abstract_classes import Button, Checkbox


class WinButton(Button):
    def paint(self):
        print('Win button')

class WinCheckbox(Checkbox):
    def paint(self):
        print('Win Checkbox')