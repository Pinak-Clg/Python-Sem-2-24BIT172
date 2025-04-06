# 1. A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a 
# program to find out number of boys and girls in the list.

def boys_and_girls():
    list = [("pinak","ram","shyam"),"ritu", "vrinda", "krisha",("elon",),"angela"]
    print("list:", list)

    boys= 0
    girls =0

    for i in list:
        if isinstance(i,tuple):
            boys += len(i)
        else:
            girls += 1

    print("number of boys:",boys)
    print("number of girls:",girls)
boys_and_girls()

# output:
# list:[('pinak', 'ram', 'shyam'), 'ritu', 'vrinda', 'krisha', ('elon',), 'angela']
# number of boys:4
# number of girls:3


# 2. A list contains tuples containing roll no., name and age of student. Write a python program to create 
# three lists separately for roll no., name and age 

def student_details():
    studentlist = [(1,"ram",18),(2,"shyam",21),(3,"vinod",19)]
    print("student list:",studentlist)

    rollno =[]
    names =[]
    ages =[]

    for i in studentlist:
        rollno.append(i[0])
        names.append(i[1])
        ages.append(i[2])

    print("Roll Numbers:",rollno)
    print("Names:",names)
    print("Ages:",ages)
student_details()

# output:
# student list:[(1, 'ram', 18), (2, 'shyam', 21), (3, 'vinod', 19)]
# Roll Numbers:[1, 2, 3]
# Names:['ram', 'shyam', 'vinod']
# Ages:[18, 21, 19]


# 3. Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of 
# days between the two dates.

from datetime import date
def dates_difference():
    date1 =(12,3,2024)
    date2 =(5,1,2017)

    print("first date:",date1)
    print("second date:",date2)

    d1 =date(date1[2],date1[1],date1[0])
    d2 =date(date2[2],date2[1],date2[0])

    diff = abs((d1 - d2).days)
    print("Number of days between two dates:",diff)
dates_difference()

# output:
# first date:(12, 3, 2024)
# second date:(5, 1, 2017)
# Number of days between two dates:2623


# 4. Create a list of tuples containing a food item and its price. Sort the tuples in descending order by 
# price.
import operator
def fooditems():
    fooditems = [("Burger", 120), ("Pizza", 2400), ("Pasta", 180)]
    print("food list:",fooditems)

    sort =sorted(fooditems, key = operator.itemgetter(1), reverse=True)
    print("sorted food list:",sort)
# fooditems()
# food list:[('Burger',120),('Pizza',2400),('Pasta',180)]
# sorted food list:[('Pizza', 2400), ('Pasta', 180), ('Burger', 120)]


# 5. Remove empty tuple(s) from the list of tuples. 

def remove_empty():
    tuple = [(),(1, 2, 3),(),(4, 5),()]
    print("Original list of tuples:",tuple)

    newtuple =[]
    for i in tuple:
        if i:
            newtuple.append(i)

    print("List after removing empty tuples:",newtuple)
remove_empty()

# output:
# Original list of tuples:[(), (1, 2, 3), (), (4, 5), ()]
# List after removing empty tuples:[(1, 2, 3), (4, 5)]


# 6. Modify an element of a tuple. 

def modify_tuple():
    t = (10,20,30,40)
    print("original tuple:",t)

    l = list(t)
    l[2] = 99 
    ans =tuple(l)

    print("Tuple after modification:", ans)
modify_tuple()

# output:
# original tuple:(10, 20, 30, 40)
# Tuple after modification:(10, 20, 99, 40)


# 7. Delete an element of a tuple.

def delete_tuple():
    t =(10,20,30,40)
    print("original tuple:",t)

    l = list(t)
    del(l[1])
    ans =tuple(l)

    print("Tuple after modification:",ans)
delete_tuple()

# output:
# original tuple:(10, 20, 30, 40)
# Tuple after modification:(10, 30, 40)
