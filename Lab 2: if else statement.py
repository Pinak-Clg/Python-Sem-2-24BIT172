# 1) Print largest and smallest values out of two.
def largestandSmallestofTwo():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if(a>b):
        print("Largest:",a)
        print("Smallest:",b)
    else:
        print("Largest:",b)
        print("Smallest:",a)
largestandSmallestofTwo()

#2) Print largest and smallest values out of three.

def largestandSmallestofThree():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    largest = max(a, b, c)
    smallest = min(a, b, c)
    
    print("Largest:", largest)
    print("Smallest:", smallest)
largestandSmallestofThree()

#3) Check whether a given number is odd or even.

def oddOrEven():
    num = int(input("Enter a number: "))
    if (num%2==0):
        print("Even")
    else:
        print("Odd")
oddOrEven()

# 4) Check whether a given number is divisible by 10 or not.

def divisibleby10():
    num = int(input("Enter a number: "))
    if num % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")
divisibleby10()

# 5) Accept age of a person. If age is less than 18, print minor otherwise Major.

def age():
    age = int(input("Enter age:"))
    if age < 18:
        print("Minor")
    else:
        print("Major")
age()

# 6) Accept a number from the user. And print number of digits in it.

def digitsinNumber():
    num = input("Enter a number:")
    print("Number of digits:",len(num))
digitsinNumber()

# 7) Accept a year value from the user. Check whether it is a leap year or not.
def leapYear():
    y = input("Enter a year:")
    num = int(y[len(y)-2]*10 + y[len(y)-1])
    if(num%4 == 0):
        print("Leap year")
    else:
        print("Not leap year")
leapYear()

# 8) Check whether a triangle is valid or not, when the three angles of the triangle are entered
# through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.
def isTriangle():
    angle1=int(input("First angle:"))
    angle2=int(input("Second angle:"))
    angle3=int(input("Third angle:"))
    if((angle1+angle2+angle3)==180):
        print("valid triangle")
    else:
        print("invalid triangle")
isTriangle()

# 9) Print absolute value of a given number.
def absolute():
    num = int(input("Enter a number:"))
    if(num >= 0):
        print(num)
    else:
        print("absolute value:",num*(-1))
absolute()

# 10) Given the length and breadth of a rectangle, write a program to find whether the are of the
# rectangle is greater than its perimeter.
def rectangleAreaPerimeter():
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    area = l*b
    peri = 2*(l+b)
    if area > peri:
        print("Area is greater than Perimeter")
    else:
        print("Area is not greater than Perimeter")
rectangleAreaPerimeter()

# 11) Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight
# line
def iscollinear():
    x1 = int(input("Enter first point x1:"))
    y1 = int(input("Enter first point y1:"))
    x2 = int(input("Enter second point x2:"))
    y2 = int(input("Enter second point y2:"))
    x3 = int(input("Enter first point x3:"))
    y3 = int(input("Enter first point y3:"))

    area = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

    if area == 0:
        print("Points are collinear")
    else:
        print("Points are not collinear")
iscollinear()

# 12) Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies
# inside the circle, on the circle or outside the circle.
def circleAndPoint():
    import math
    cx = int(input("Enter center coordinate x:"))
    cy = int(input("Enter center coordinate y:"))

    r = int(input("Enter radius:"))
    px = int(input("Enter point coordinate px:"))
    py = int(input("Enter point coordinate py:"))
   
    dist = math.sqrt((px - cx)**2 + (py - cy)**2)
    
    if dist<r:
        print("Point lies inside the circle")
    elif dist==r:
        print("Point lies on the circle")
    else:
        print("Point lies outside the circle")
circleAndPoint()

# 13) Convert number 0 to 19 to its equivalent words. E.g. 0 → zero, 19→nineteen.
def numbertowords():
    numarray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
                   "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
                   "eighteen", "nineteen"]
    num=int(input("Enter a number between 0 and 19:"))
    if 0 <= num <= 19:
        print(numarray[num])
    else:
        print("invalid number")
numbertowords()

# 14) Accept marks of three subjects. Print total and average along with whether a candidate has
# passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a
# subject wise grade based on the following table:

def calculate_gread(n):
    if n == "Absent":
        n = "NA"
    elif n<=39:
        n = "F"
    elif n<=44:
        n = "P"
    elif n<=49:
        n = "C"
    elif n<=54:
        n = "B"
    elif n<=59:
        n = "B+"
    elif n<=69:
        n = "A"
    elif n<=79:
        n = "A+"
    else:
        n = "O"
    return n


def result():
    sub1 = int(input("Subject1 marks:"))
    sub2 = int(input("Subject2 marks:"))
    sub3 = int(input("Subject3 marks:"))
    total= sub1 + sub2 + sub3
    average = total/3
    print("Total:", total)
    print("Average:", average)
    
    print("Subject 1 gread:",calculate_gread(sub1))
    print("Subject 1 gread:",calculate_gread(sub2))
    print("Subject 1 gread:",calculate_gread(sub3))
result()
