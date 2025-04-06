# 1.Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.

def list_modification():
    odd = [1,3,5,7,9]
    even = [2,4,6,10]
    
    odd[2] = even
    print("Replacing the third element of odd integers with a list of 4 even integers:",odd)

    flatterned = []
    for i in odd:
        if isinstance(i,list):
            flatterned.extend(i)
        else:
            flatterned.append(i)

    print("Flatterned list:",flatterned)

    flatterned.sort()

    print("sorted list:",flatterned)

list_modification()

# Output:
# Replacing the third element of odd integers with a list of 4 even integers: [1, 3, [2, 4, 6, 10], 7, 9]
# Flatterned list: [1, 3, 2, 4, 6, 10, 7, 9]
# sorted list: [1, 2, 3, 4, 6, 7, 9, 10]


# 2.Generate 20 random integers and store them in a list.Accept a number from the user and print 
# position of all occurrences of that number in the list. 

import random

def find_occurance():
    num = [random.randint(1, 50) for i in range(20)]
    print("Generated list of 20 random numbers:",num)

    n = int(input("Enter number to find occurrences: "))

    ans = []
    for i in range(20):
        if num[i]==n:
            ans.append(i)

    
    print("The number occurs at:",ans)

# find_occurance()

# Sample Output:
# Generated list of 20 random numbers: [4, 27, 15, 27, 8, 10, 33, 21, 18, 27, 5, 12, 14, 27, 11, 2, 27, 44, 19, 6]
# Enter number to find occurrences: 27
# The number occurs at: [1, 3, 9, 13, 16]


# 3.Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list. 

def remove_duplicate():
    num = [random.randint(1, 30) for i in range(50)]
    print("list:", num)

    unique=list(set(num))
    print("List after removing duplicates:",unique)

# remove_duplicate()

# Sample Output:
# list: [14, 6, 20, 13, 14, 29, 17, 7, 5, 11, 5, 12, 6, 2, 3, 21, 18, 17, 24, 29, 4, 13, 6, 2, 9, 15, 27, 7, 14, 16, 3, 1, 30, 11, 2, 18, 26, 5, 24, 25, 10, 22, 7, 6, 21, 4, 16, 12, 19, 8]
# List after removing duplicates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30]


# 4.Generate 30 random numbers and put them in a list. Create two more lists – one containing only 
# +ve numbers and another with –ve nos.

def filterlist():
    num = [random.randint(-50, 50) for i in range(30)]
    print("list:", num)

    positive = []
    negative = []

    for i in num:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)

    print("list of positive numbers:",positive)
    print("list of negative numbers:",negative)

filterlist()

# Output:
# list: [-27, 15, -7, -1, -45, -12, -20, 23, -32, -26, 33, 45, -47, 10, 25, 19, 4, 17, 8, -38, 2, -16, -11, 1, -14, 3, -19, -21, 14, -2]
# list of positive numbers: [15, 23, 33, 45, 10, 25, 19, 4, 17, 8, 2, 1, 3, 14]
# list of negative numbers: [-27, -7, -1, -45, -12, -20, -32, -26, -47, -38, -16, -11, -14, -19, -21, -2]


# 5.A list contains 5 strings. Convert all these strings to uppercase.

def upper_string():
    strings = ["Pdeu","hello","pinak","WORLD","python"]
    
    for i in range(5):
        strings[i] = strings[i].upper()

    print("List after converting in uppercase:",strings)

# upper_string()

# Sample Output:
# List after converting in uppercase: ['PDEU', 'HELLO', 'PINAK', 'WORLD', 'PYTHON']


# 6.Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.

def fahrenheit_celsius():
    fahrenheit = [32,68,77,104,50]
    print("Temperatures in F:",fahrenheit)

    celsius = []
    for i in fahrenheit:
        celsius.append((i-32)*5/9)

    print("Temperatures in C:",celsius)

# fahrenheit_celsius()

# Sample Output:
# Temperatures in F: [32, 68, 77, 104, 50]
# Temperatures in C: [0.0, 20.0, 25.0, 40.0, 10.0]


# 7. Write a menu-driven program to implement the stack data structure.

def stack():
    stack = []

    while True:
        print("Stack Operations:")
        print("1.push")
        print("2.pop")
        print("3.print")
        print("4. Exit")

        n = int(input("Enter n:"))

        if n == 1:
            ele = input("Enter element: ")
            stack.append(ele)
            print("stack after push:",stack)

        elif n == 2:
            if stack:
                poppedElement = stack.pop()
                print("popped element:",poppedElement)

        elif n == 3:
            print("current Stack:",stack)

        else:
            print("Exiting program")
            break

# stack()

# Sample Output:
# Stack Operations:
# 1.push
# 2.pop
# 3.print
# 4. Exit
# Enter n:1
# Enter element: apple
# stack after push: ['apple']
# Stack Operations:
# 1.push
# 2.pop
# 3.print
# 4. Exit
# Enter n:1
# Enter element: ball
# stack after push: ['apple', 'ball']
# Stack Operations:
# 1.push
# 2.pop
# 3.print
# 4. Exit
# Enter n:2
# popped element: ball
# Stack Operations:
# 1.push
# 2.pop
# 3.print
# 4. Exit
# Enter n:3
# current Stack: ['apple']
# Stack Operations:
# 1.push
# 2.pop
# 3.print
# 4. Exit
# Enter n:4
# Exiting program


# Take two lists of numbers.Create third list of numbers for only those numbers from first list which 
# are not there in 2nd list (use list comprehension).

def lists_difference():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [2, 4, 6, 8]

    print("List1:", l1)
    print("List2:", l2)

    ans = [i for i in l1 if i not in l2]
    print("Numbers from first list not in second list:",ans)

# lists_difference()

# Sample Output:
# List1: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# List2: [2, 4, 6, 8]
# Numbers from first list not in second list: [1, 3, 5, 7, 9]
