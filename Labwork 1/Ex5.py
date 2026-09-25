colors = ["Red", "Blue", "Green", "Yellow", "Black"]

color = input("What is your favorite color? ")

if color in colors:
    print("Your color is at index", colors.index(color), "in my list")
else:
    print("Sorry, I could not find your color")