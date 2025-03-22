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


# list_modification()


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


# 3.Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list. 


def remove_duplicate():
    num = [random.randint(1, 30) for i in range(50)]
    print("list:", num)

    unique=list(set(num))
    print("List after removing duplicates:",unique)
# remove_duplicate()


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
# filterlist()

# 5.A list contains 5 strings. Convert all these strings to uppercase.


def upper_string():
    strings = ["Pdeu","hello","pinak","WORLD","python"]
    
    for i in range(5):
        strings[i] = strings[i].upper()

    print("List after converting in uppercase:",strings)
# upper_string()

# 6.Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.


def fahrenheit_celsius():
    fahrenheit = [32,68,77,104,50]
    print("Temperatures in F:",fahrenheit)

    celsius = []
    for i in fahrenheit:
        celsius.append((i-32)*5/9)

    print("Temperatures in C:",celsius)
# fahrenheit_celsius()

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

#Take two lists of numbers.Create third list of numbers for only those numbers from first list which 
# are not there in 2nd list (use list comprehension).


def lists_difference():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [2, 4, 6, 8]

    print("List1:", l1)
    print("List2:", l2)

    ans = [i for i in l1 if i not in l2]
    print("Numbers from first list not in second list:",ans)
# lists_difference()




        
 


    
