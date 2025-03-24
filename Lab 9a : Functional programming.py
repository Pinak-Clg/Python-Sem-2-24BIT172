# 1.Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.

def fun():
    print("Hello")

def disp():
    print("World")

def msg():
    print("Python")

lst = [fun(),disp(),msg()]

for i in lst:
    i

# 2.Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists. (hint: use map and lambda functions)

def add_list():
    lst1 = [1,2,3,4,5,6]
    lst2 = [6,5,4,3,2,1]


    ans = list(map(lambda x,y:x+y,lst1,lst2))
    print("list 1:",lst1)
    print("list 2:",lst2)
    print("List after addition:",ans)
add_list()


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

# 4.Consider the following list:
# lst = ['madam','Python',"malayalam",12321]
# Write a program to print those strings which are palindromes.

def check_palindromes():

    lst = ['madam','Python',"malayalam",12321]
    def ispalindrome(s):
        a =str(s)
        b = a[::-1]
        return True if a==b else False

    # ans = list(filter(lambda x:ispalindrome(x),lst))
    ans = list(filter(lambda x:str(x)==str(x)[::-1],lst))
    print("\nList:",lst)
    print("Availale palindrome in list:", ans)

check_palindromes()


# 5.A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.

def filter_list():

    name = ["sameer","darshit","larry","satoshi nakamoto","husan janhuang","chintan bhatt","mark zuckerberge","bill"]

    ans = list(filter(lambda x:len(x)>8,name))
    print("\nNames:", name)
    print("Names with length>8:",ans)

filter_list()
