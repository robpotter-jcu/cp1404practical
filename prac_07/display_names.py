"""
CP1404 Practical
Program to display a list of names on separate labels.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DisplayNamesApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Tom", "Dick", "Harry"]

    def build(self):
        self.title = "Display Names"
        self.root = Builder.load_file("display_names.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.label.add_widget(temp_label)


DisplayNamesApp().run()
