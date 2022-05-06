from ..abstract_classes import Button, Checkbox


class MacButton(Button):
    def paint(self):
        print('Mac button')


class MacCheckbox(Checkbox):
    def paint(self):
        print('Mac Checkbox')