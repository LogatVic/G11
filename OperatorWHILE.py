# Variables definition
def letsgo(a,b,c):
#Loop with condition
    while a<b:
        a+=c
        if a<b:
            print(a, "- Not now, be patient!")
        elif a > b:
            print("You have received figure", a, "- Point busting!")
        else:
            print("While not, you came! -", a)
# Input data block
try:
    letsgo(
         int(input("Input initial integer figure:\n")),
         int(input("Input final integer figure:\n")),
         int(input("Indicate the augment as an integer figure:\n")))
# Protection from not-integer figure input
except ValueError:
    print("\nYours figure is not integer! Please begin again.")