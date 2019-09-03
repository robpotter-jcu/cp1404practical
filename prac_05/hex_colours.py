"""
CP1404 Practical
Hexadecimal colour lookup
"""

COLOUR_CODES = {"blue1": "#0000ff", "brown1": "#ff4040", "DarkOrange1": "#ff7f00", "DarkOrchid1": "#bf3eff",
                "DeepPink1": "#ff1493", "gold1": "#ffd700", "gray1": "#030303", "green1": "#00ff00",
                "maroon1": "#ff34b3", "yellow1": "#ffff00"}
colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
