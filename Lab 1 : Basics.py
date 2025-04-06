#mathematical operation
a = 5
b = 6

#sum
print(a+b)
# output:11

#subtract
print(a-b)
# output:-1

#multiplication
print(a*b)
# output:30

#division
print(a/b)
# output:0.8333333333333334

def hourtominutes():
    hours = int(input("Hours: "))
    print("minutes:",hours*60)

# output:
# Hours:2
# minutes:120

def minutestohours():
    minutes = int(input("minutes: "))
    print("hours:",minutes/60)

# output: 
# minutes:180
# hours:3.0

def DtoRs():
    dollars = int(input("dollars: "))
    print("rupees:",dollars*48)

# output:
# dollars:5
# rupees:240

def RstoD():
    rupees = int(input("rupees:"))
    print("dollars:",rupees/48)

# output:
# rupees:480
# dollars:10.0

def DtoPound():
    dollars = int(input("dollars:"))
    rupees = dollars*48
    print("pounds:",rupees/70)

# output:
# dollars:7
# pounds:4.8

def gramsToKg():
    grams = int(input("grams:"))
    print("kilograms:",grams/1000)

# output:
# grams:1500
# kilograms:1.5

def kgToGrams():
    kg = int(input("kilograms:"))
    print("grams:",kg*1000)

# output:
# kilograms:2
# grams:2000

def bytesconvert():
    bytes=int(input("bytes: "))
    print("KB:",bytes/1024)
    print("MB:",bytes/(1024*1024))
    print("GB:",bytes/(1024*1024*1024))

# output:
# bytes:1048576
# KB:1024.0
# MB:1.0
# GB:0.0009765625

def celsiusToFahrenheit():
    C=int(input("Celsius:"))
    print("Fahrenheit:",(9/5*C)+32)

# output:
# Celsius:25
# Fahrenheit:77.0

def fahrenheitToCelsius():
    F=int(input("Fahrenheit:"))
    print("Celsius:",5/9*(F-32))

# output:
# Fahrenheit:98
# Celsius:36.666666666666664

def Interest():
    P=int(input("Principal:"))
    R=int(input("Rate:"))
    T=int(input("Time:"))
    print("Interest:",(P*R*T)/100)

# output:
# Principal:1000
# Rate:5
# Time:2
# Interest:100.0

def squareAreaPeri():
    L=int(input("Side length:"))
    print("Area:",L*L)
    print("Perimeter:",4*L)

# output:
# Side length:5
# Area:25
# Perimeter:20

def rectangleAreaPeri():
    L=int(input("Length: "))
    B=int(input("Breadth: "))
    print("Area",L*B)
    print("Perimeter:",2*(L+B))

# output:
# Length:10
# Breadth:4
# Area40
# Perimeter:28

def circleArea():
    r=int(input("Radius: "))
    print("Area:",(22/7)*r*r)

# output:
# Radius:7
# Area:154.0

def triangleArea():
    h = float(input("Height: "))
    b = float(input("Base: "))
    print("Area:",(h*b)/2)

# output:
# Height:10
# Base:8
# Area:40.0

def calculateSalary():
    gross=int(input("Gross Salary: "))
    print("Net Salary:",gross+0.1*gross-0.03*gross)

# output:
# Gross Salary:10000
# Net Salary:10700.0

def NetSales():
    gross = float(input("Gross Sales: "))
    print("Net Sales:",gross-(0.1*gross))

# output:
# Gross Sales:5000
# Net Sales:4500.0

def averageofsubjects():
    sub1 = int(input("Subject 1 marks: "))
    sub2=int(input("Subject 2 marks: "))
    sub3 = int(input("Subject 3 marks: "))
    total = sub1 + sub2 + sub3
    print("Total:",total)
    print("Average:",total/3)

# output:
# Subject 1 marks:70
# Subject 2 marks:80
# Subject 3 marks:90
# Total:240
# Average:80.0

def swapValues():
    a =input("Enter first value: ")
    b = input("Enter second value: ")
    temp = a
    a = b
    b = temp
    print("First value:",a)
    print("Second value:",b)

# output:
# Enter first value:apple
# Enter second value:banana
# First value:banana
# Second value:apple






