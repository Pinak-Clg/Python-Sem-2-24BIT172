#mathematical operation
a = 5
b = 6

#sum
print(a+b)

#subtract
print(a-b)

#multiplication
print(a*b)

#division
print(a/b)


def hourtominutes():
    hours = int(input("Hours: "))
    print("Minutes: ",hours*60)
hourtominutes()

def minutestohours():
    minutes = int(input("minutes: "))
    print("hours: ",minutes/60)
minutestohours()

def DtoRs():
    dollars = int(input("dollars: "))
    print("rupees: ",dollars*48)
DtoRs()

def RstoD():
    rupees = int(input("rupees:"))
    print("dollars:",rupees/48)
RstoD()

def DtoPound():
    dollars = int(input("dollars:"))
    rupees = dollars*48
    print("pounds:", rupees/70)
DtoPound()

def gramsToKg():
    grams = int(input("grams:"))
    print("kilograms:", grams/1000)
gramsToKg()

def kgToGrams():
    kg = int(input("kilograms:"))
    print("grams:", kg*1000)
kgToGrams()

def bytesconvert():
    bytes=int(input("bytes: "))
    print("KB:", bytes/1024)
    print("MB:",bytes/(1024*1024*1024))
    print("GB:", bytes/(1024*1024*1024))
bytesconvert()

def celsiusToFahrenheit():
    C = int(input("Celsius:"))
    print("Fahrenheit:",(9/5*C)+32)
celsiusToFahrenheit()

def fahrenheitToCelsius():
    F = int(input("Fahrenheit:"))
    print("Celsius:", 5/9*(F-32))
fahrenheitToCelsius()

def Interest():
    P = int(input("Principal:"))
    R = int(input("Rate:"))
    T = int(input("Time:"))
    print("Interest: ",(P*R*T)/100)
Interest()

def squareAreaPeri():
    L = int(input("Side length:"))
    print("Area:", L*L)
    print("Perimeter:", 4*L)
squareAreaPeri()

def rectangleAreaPeri():
    L = int(input("Length: "))
    B = int(input("Breadth: "))
    print("Area",L*B)
    print("Perimeter:",2*(L+B))
rectangleAreaPeri()

def circleArea():
    r = int(input("Radius: "))
    print("Area: ",(22/7)*r*r)
circleArea()

def triangleArea():
    h = float(input("Height: "))
    b = float(input("Base: "))
    print("Area:",(h*b)/2)
triangleArea()

def calculateSalary():
    gross = int(input("Gross Salary: "))
    print("Net Salary:",gross+0.1*gross-0.03*gross)
calculateSalary()

def NetSales():
    gross = float(input("Gross Sales: "))
    print("Net Sales: ", gross-(0.1*gross))
NetSales()

def averageofsubjects():
    sub1 = int(input("Subject 1 marks: "))
    sub2 = int(input("Subject 2 marks: "))
    sub3 = int(input("Subject 3 marks: "))
    total = sub1 + sub2 + sub3
    print("Total: ", total)
    print("Average: ", total / 3)
averageofsubjects()

def swapValues():
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    temp = a
    a = b
    b = temp
    print("First value: ", a)
    print("Second value: ", b)
swapValues()






