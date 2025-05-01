#1.Print all alphabets in upper case and in lower case.

def printalphabets():

    print("lowercase:")
    for i in range(97,123):
        print(chr(i))

    print("uppercase:")
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        print(i)
        
# printalphabets()

# Output:
# lowercase:
# a
# b
# c
# d
# e
# f
# g
# h
# i
# j
# k
# l
# m
# n
# o
# p
# q
# r
# s
# t
# u
# v
# w
# x
# y
# z
# uppercase:
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J
# K
# L
# M
# N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y
# Z

#2.Print a multiplication table of a given number. 

def table():

    n = int(input("Enter a number:"))

    for i in range(1,11):
        print(n,"x",i,"=",i*n)
# table()

# Sample Output:
# Enter a number:5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#3.Count no. of alphabets and no. of digits in any given string.

def noAlphabet_noDigits():
    s = input("Enter a string:")
    digit = 0
    alpha = 0
    for i in s:
        if(i.isdigit()):
            digit += 1
        else:
            alpha+=1
    print("number of alphabet is",alpha,"and number of digits is",digit)

# noAlphabet_noDigits()

# Output:
# Enter a string:abc123
# number of alphabet is 3 and number of digits is 3

#4.Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 1/2) + 1):
        if n % i == 0:
            return False
    return True

#perfect number sum of factor 0
def perfect_no(n):
    sum = 0
    for i in range(1,n):
        if (n%i==0):
            sum +=i
    if sum==n:
        return True
    
    else:
        return False

def isarmstrong(n):
    s = str(n)
    power = len(s)
    sum = 0
    for i in s:
        sum+=int(i)**power
    if sum==n:
        return True
    else:
        return False

def ispalindrome(n):
    s1 = str(n)
    s2 = s1[::-1]
    if s1==s2:
        return True
    else:
        return False

def numberproperties():
    n = int(input("Enter a number: "))

    if isprime(n):
        print(n,"is a prime number")
    else:
        print(n,"is not prime number")

    if perfect_no(n):
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")

    if isarmstrong(n):
        print(n,"is an armstrong number")
    else:
        print(n,"is not armstrong number")

    if ispalindrome(n):
        print(n,"is a palindrome number")
    else:
        print(n,"is not a palindrome number")

# numberproperties()

# Sample Output:
# Enter a number:28
# 28 is not prime number
# 28 is a perfect number
# 28 is not armstrong number
# 28 is not a palindrome number

# 5. Generate all Pythagorean Triplets with side length <= 30.

def pythagoreanTriplets():
    print("Pythagorean Triplets (a,b,c):")
    
    for a in range(1,31):
        for b in range(a,31): 
            for c in range(b,31):
                if a**2 + b**2 == c**2:
                    print([a,b,c])

# pythagoreanTriplets()

# Sample Output:
# Pythagorean Triplets (a,b,c):
# [3, 4, 5]
# [5, 12, 13]
# [6, 8, 10]
# [7, 24, 25]
# [8, 15, 17]
# [9, 12, 15]
# [10, 24, 26]
# [12, 16, 20]
# [15, 20, 25]
# [18, 24, 30]
# [20, 21, 29]

# 6. Print 24 hours of the day with suitable suffixes like AM, PM, Noon, and Midnight.

def hours24():
    for h in range(24):
        if h == 0:
            print("12 Midnight")
        elif h == 12:
            print("12 Noon")
        elif h < 12:
            print(h,"AM")
        else:
            print(h-12,"PM")

# hours24()

# Sample Output:
# 12 Midnight
# 1 AM
# 2 AM
# 3 AM
# 4 AM
# 5 AM
# 6 AM
# 7 AM
# 8 AM
# 9 AM
# 10 AM
# 11 AM
# 12 Noon
# 1 PM
# 2 PM
# 3 PM
# 4 PM
# 5 PM
# 6 PM
# 7 PM
# 8 PM
# 9 PM
# 10 PM
# 11 PM

# 7.Print factorial of a given number.

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

# print(fact(5))

# Sample Output:
# 120

# 8.Print nCr and nPr.

def nPr(n,r):
    return fact(n)/fact(n - r)

# Function to calculate nCr (Combination)
def nCr(n,r):
    return fact(n)/(fact(r)*fact(n - r))

# print(nPr(10,7))
# print(nCr(10,4))

# Sample Output:
# 604800.0
# 210.0

# 9.Print N natural nos. in reverse.

def reversenaturalno():
    n = int(input("Enter a number:"))
    while n>=0:
        print(n)
        n=n-1
# reversenaturalno()

#Output:
# Enter a number:5
# 5
# 4
# 3
# 2
# 1
# 0

# 10.Generate N numbers of Fibonacci series.

def fibonacci(n,first=0,second=1,count=0):
    if count < n:
        print(first)
        fibonacci(n,second,first+second,count+1)
# n = int(input("Enter a number:"))
# fibonacci(n)

#Output:
# Enter a number:6
# 0
# 1
# 1
# 2
# 3
# 5


# Calculate sin(x) using Taylor series
x_deg = float(input("Enter angle in degrees: "))
x = x_deg * 3.14159 / 180  # Convert to radians

terms = 5  # Number of terms in the series
sin_x = 0
sign = 1

for i in range(1,2*terms,2):
    term = (x**i) / factorial(i)
    sin_x += sign * term
    sign *= -1

print("sin(x) =", sin_x)

# Sample Input/Output:
# Input: 30
# Output: sin(x) = 0.4999999918690232

