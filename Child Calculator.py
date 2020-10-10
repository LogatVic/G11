print("CHILD CALCULATOR")
print("Hello, my little Friend!")
X=int(input("Could you please input the first number: "))
Y=int(input("Could you please input second number: "))
what=input("And now choice what do you like to do - sign (+, -, *, /): ")
C=None
if what=="+":
    C=X+Y
elif what=="-":
    C=X-Y
elif what=="*":
    C=X*Y
elif what=="/":
    if Y==0:
            print("WARNING!: Division by ZERO is impossible, please try somewhat else")
    else: C=X/Y
print("Here's the RESULT: " + str(C))