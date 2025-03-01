HEX_COLOURS = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Apricot": "#fbceb1",
    "Bitter Lemon": "#cae00d",
    "Bittersweet": "#fe6f5e",
    "Black Coffee": "#3b2f2f",
    "BlanchedAlmond": "#ffebcd",
    "Blond": "#faf0be",
}

print("Hex Colour Lookup")
colour_name = input("Enter a colour name: ").strip()
while colour_name:
    colour_key = colour_name.replace(" ", "").title()
    if colour_key in HEX_COLOURS:
        print(f"The hex code for {colour_key} is {HEX_COLOURS[colour_key]}")
    else:
        print("Invalid colour name. Try again.")
    colour_name = input("Enter a colour name: ").strip()
print("Goodbye!")
