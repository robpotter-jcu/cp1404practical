"""
CP1404 Practical
Kivy GUI program for square a number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """Kivy app for square a number."""
    def build(self):
        """Build Kivy app from kv file."""
        Window.size = (750, 200)
        self.title = "Square Number"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call)
        output result to label widget."""
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
