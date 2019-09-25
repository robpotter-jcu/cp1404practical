"""
CP1404 Practical
Kivy GUI program for box layout demo
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app for box layout demo."""
    def build(self):
        """Build Kivy app from kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting format that includes input."""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle clearing of input and output text fields."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
