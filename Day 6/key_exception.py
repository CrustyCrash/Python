colours = {
    1: "red",
    2: "blue",
    3: "orange"
}
try:
    key = int(input("Enter key: "))
    print(colours[key])

except KeyError:
    print("Colour not found")
    exit()
