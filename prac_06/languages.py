"""
CP1404 Practical
Client code for programming language.
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Program to print the name of dynamically typed programming languages."""
    cpp = ProgrammingLanguage("C++", "Static", False, 1983)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [cpp, java, python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
