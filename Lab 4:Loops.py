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

#2.Print a multiplication table of a given number. 

def table():

    n = int(input("Enter a number:"))

    for i in range(1,11):
        print(n,"x",i,"=",i*n)
# table()


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

# 5.Generate all Pythagorean Triplets with side length <= 30.

# 5. Generate all Pythagorean Triplets with side length <= 30.

def pythagoreanTriplets():
    print("Pythagorean Triplets (a,b,c):")
    
    for a in range(1,31):
        for b in range(a,31): 
            for c in range(b,31):
                if a**2 + b**2 == c**2:
                    print([a,b,c])

# pythagoreanTriplets()

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

# 7.Print factorial of a given number.

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

# print(fact(5))

# 8.Print nCr and nPr.

def nPr(n,r):
    return fact(n)/fact(n - r)

# Function to calculate nCr (Combination)
def nCr(n,r):
    return fact(n)/(fact(r)*fact(n - r))

# print(nPr(10,7))
# print(nCr(10,4))


# 9.Print N natural nos. in reverse.

def reversenaturalno():
    n = int(input("Enter a number:"))
    while n>=0:
        print(n)
        n=n-1
# reversenaturalno()

# 10.Generate N numbers of Fibonacci series.

def fibonacci(n,first=0,second=1,count=0):
    if count < n:
        print(first)
        fibonacci(n,second,first+second,count+1)
# n = int(input("Enter a number:"))
# fibonacci(n)






















