
# 1. Write a program that converts words present in a list into uppercase and stores them in a set. 

def list_to_set():
    word = ["apple","google","microsoft","atlassian","meta","google"]
    print("list:",word)

    wordset = set()
    for i in word:
        wordset.add(i.upper())

    print("Set with uppercase:",wordset)
list_to_set()


# 2. Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how 
# many of these numbers are less than 30. Delete all numbers that are greater than 35.

import random

def set_modification():
    num =set()
    for i in range(10):
        num.add(random.randint(15,45))

    print("set:",num)

    count = 0
    for i in num:
        if i<30:
            count+=1
    
    print("numbers less than 30:",count)
    ans = set()
    for i in num:
        if i<=35:
            ans.add(i)

    
    print("Set after removing numbers >35:",ans)
set_modification()


# 3. Create an empty set. Write a program that adds five new names to this set, modifies one existing 
# name and deletes two names from it.

def nameset():
    name = set()
    name.update(["pinak", "rudra", "deep", "raj", "kiara"])
    print("set:",name)

    name.remove("kiara")
    name.add("alia")
    print("set after modifying a name:",name)

    name.remove("pinak")
    name.remove("rudra")
    print("set after deleting two names:",name)
nameset()



# 4. A set contains names which begin either with A or with B. Write a program to separate out the 
# names into two sets, one containing names beginning with A and another with B. 


def separatenames():
    name = {"Aman","Ali", "Bili","Brijesh"}
    print("set:",name)

    setA = set()
    setB = set()

    for i in name:
        if i[0]=="A":
            setA.add(i)
        elif i.startswith("B"):
            setB.add(i)

    print("Names A:",setA)
    print("Names B:",setB)
separatenames()


