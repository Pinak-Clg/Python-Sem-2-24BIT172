# 1.Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.

def fun():
    print("Hello")

def disp():
    print("World")

def msg():
    print("Python")

lst = [fun, disp, msg]

for i in lst:
    i()

# output:
# Hello
# World
# Python


# 2.Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists.

def add_list():
    lst1 = [1,2,3,4,5,6]
    lst2 = [6,5,4,3,2,1]

    ans = list(map(lambda x,y:x+y,lst1,lst2))
    print("list 1:",lst1)
    print("list 2:",lst2)
    print("List after addition:",ans)
add_list()

# output:
# list 1:[1, 2, 3, 4, 5, 6]
# list 2:[6, 5, 4, 3, 2, 1]
# List after addition:[7, 7, 7, 7, 7, 7]


# 3.Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.

import random
def squarelist():
    lst = []
    for i in range(10):
        lst.append(random.randint(-15,15))
    print("\nList:", lst)

    ans = list(map(lambda x:x*x,lst))

    print("List after squaring elements:", ans)
squarelist()

# output (sample):
# List:[-3, 5, -10, 14, 2, -15, 13, 7, -8, 9]
# List after squaring elements:[9, 25, 100, 196, 4, 225, 169, 49, 64, 81]


# 4.Consider the following list: lst = ['madam','Python',"malayalam",12321]
# Write a program to print those strings which are palindromes.

def check_palindromes():
    lst = ['madam','Python',"malayalam",12321]
    ans = list(filter(lambda x:str(x)==str(x)[::-1],lst))
    print("\nList:",lst)
    print("Availale palindrome in list:", ans)
check_palindromes()

# output:
# List:['madam', 'Python', 'malayalam', 12321]
# Availale palindrome in list:['madam', 'malayalam', 12321]


# 5.A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.

def filter_list():
    name = ["sameer","darshit","larry","satoshi nakamoto","husan janhuang","mark zuckerberge","bill"]

    ans = list(filter(lambda x:len(x)>8,name))
    print("\nNames:", name)
    print("Names with length>8:",ans)
filter_list()

# output:
# Names:['sameer', 'darshit', 'larry', 'satoshi nakamoto', 'husan janhuang', 'mark zuckerberge', 'bill']
# Names with length>8:['satoshi nakamoto', 'husan janhuang', 'mark zuckerberge']
