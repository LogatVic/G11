def matching(a, b):
    for i in b:
        count = a.count(i)
        if count >= 1:
            print("letter:", i)
            print("The letter matches:", count, "time(s)")
        else:
            print("Your letter is absent in your text!")
try:
    matching(str(input("Input your text: \n")).lower(),
            str(input("Input the letter you matching in your text: \n")).lower())
except ValueError: print("The end.")
