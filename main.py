print("TASK NAME: THE ANALYSIS OF RANDOM SAMPLING OF 5 INTEGER FIGURES FROM 0 to 9")

import random
list1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
list2 = random.sample(list1, 5)
print("The result of random sampling of 5 integers from 0 to 9 is:", list2)
print("RANDOM FIGURES LIST ANALYSIS:")
for i in list2:
    if i == 0:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 0 is absent in the list")

for i in list2:
    if i == 1:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 1 is absent in the list")

for i in list2:
    if i == 2:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 2 is absent in the list")

for i in list2:
    if i == 3:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 3 is absent in the list")

for i in list2:
    if i == 4:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 4 is absent in the list")

for i in list2:
    if i == 5:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 5 is absent in the list")

for i in list2:
    if i == 6:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 6 is absent in the list")

for i in list2:
    if i == 7:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 7 is absent in the list")

for i in list2:
    if i == 8:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 8 is absent in the list")

for i in list2:
    if i == 9:
        z = list2.index(i) + 1
        print("Figure",i, "occupies position No",z, "in the list")
        break
else:
    print("Figure 9 is absent in the list")
