"""
CP1404 Practical
Class code for programming language.
"""


class ProgrammingLanguage:
    """Represents a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns true of false if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a programming language object."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)


def run_tests():
    """Run tests on programming language class."""
    cpp = ProgrammingLanguage("C++", "Static", False, 1983)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [cpp, java, python, ruby, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
