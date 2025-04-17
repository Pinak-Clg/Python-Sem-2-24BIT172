'''
Solution author : Pinak 
Roll No : 24BIT172

Format:
1.Problem
2.code(python)
3.Output

'''



# 1) Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase
# and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample string.

def count_lower_upper():
    
    s = input("Enter a string:")
    lower=0
    upper=0
    for ch in s:
        if ch.islower():
            lower += 1
        else:
            upper += 1
    
    result={"lower":lower,"upper":upper}
    print("Result:",result)

# count_lower_upper()

# Output:
# Enter a string: HelloWorld123
# Result:{'lower':7,'upper':3}

# 2) Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, 
# where n is digit received by the function. test the function for digits 4 to 7.

def compute(n):
    value = n + n**2 + n**3 + n**4
    print("Value:",value)
compute(4)
compute(5)
compute(6)
compute(7)

# Output:
# Value: 340
# Value: 780
# Value: 1554
# Value: 2800

# 3).Write a program that defines a function create_array() to create and return a 3D array whose 
# dimensions are passed to the function. Also initialize each element of this aray to a value passed to 
# the function. e.g. create_array(3,4,5,n) where first three arguments are 3D array dimensions and 4th 
# value is for initialing each value of the 3D array.

def create_array(x, y, z, value):
    arr = [[[value for i in range(z)] for i in range(y)] for i in range(x)]
    print("3D array:",arr)
    # for i in range(x):
    #     print("\n")
    #     for j in range(y):
    #         print(arr[i][j])
create_array(2, 2, 2, 7)

# output:
# 3D array: [[[7, 7], [7, 7]], [[7, 7], [7, 7]]]

# 4. Write a program that defines a function sum_avg() to accept marks of five subjects and calculates 
# total and average. It should return  directly both values. 

# def sum_avg():
#     sum = 0;
#     for i in range(5):
#         a = int(input("Enter the marks:"))
#         sum += a
#     return [sum,sum/5]
# a = sum_avg()
# print(a)

# output:
# Enter the marks:100
# Enter the marks:98
# Enter the marks:99
# Enter the marks:97
# Enter the marks:98
# [492, 98.4]


# 5. Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a 
# given string is pangram or not, through a user-defined function ispangram(). Test the function with 
# “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal 
# jewels”.

import string
def ispangram(s):
    mainString = set(string.ascii_lowercase)
    s = set(s.lower())
    return mainString <= s

print(ispangram('abcdefghij klmnopqrstuvwxyz'))

# output:
# True

# 6) Function to create and return list of (x,x^2,x^3) tuples from 1 to given end value.
def create_tuples(n):
    List = []
    for x in range(1, n+1):
        List.append((x, x**2, x**3))
    return List
print(create_tuples(5))

# Output:
# List:[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]

# 7) Check if a string is a palindrome(ignore spaces and case).
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

ispalindrome("Madam")
ispalindrome("pinak thummar")

# Output:
# Palindrome
# Not a palindrome

# 8)Write a program that defines a function convert() that receives a string containing a sequence of 
# whitespace separated words and returns a string after removing all duplicate words and sorting.

def convert(s):
    
    words = s.split()
    ans = sorted(set(words))
    newstr = " ".join(ans)
    return newstr
    
print(convert("Iron steel copper Iron platinum gold"))

# Output:
# Input : Iron steel copper Iron platinum gold
# result: Iron copper gold platinum steel

 
# 9. Write a program that defines a function count_alpha_digits() that accepts a string and calculates the 
# number of alphabets and digits in it. It should return these values as a dictionary.

def count_alpha_digits(s):
    
    alpha = 0
    digit = 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digit += 1
    
    return {"alphabets": alpha, "digits": digit}
    
print(count_alpha_digits("Hello1234"))

# output:
# {'alphabets': 5, 'digits': 4}



# 10. Write a program that defines a function called frequency() which computes the frequency of words 
# present in a string passed to it. The frequencies should be returned in sorted order of words in the 
# string. 

# def frequency(s):



# 11. Write a function create_list() that creates and returns a list which is an intersection of two lists 
# passed to it. 

def create_list():
    list1 = [1,2,3,4,5,7]
    list2 = [2,3,4,8,9,10]
    intersection = [x for x in list1 if x in list2]
    print("Intersection list:",intersection)
create_list()

# output:
# Intersection list: [2, 3, 4]

