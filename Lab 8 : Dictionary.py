# 1. Write a program to create three dictionaries and concatenate them to create fourth dictionary.

def concatenate_dictionaries():
    dict1 = {"a":121,"b":24}
    dict2 = {"c":368,"d":440}
    dict3 = {"e":505,"f":68}

    print("dictionary 1:",dict1)
    print("dictionary 2:",dict2)
    print("dictionary 3:",dict3)

    ans = {}
    ans.update(dict1)
    ans.update(dict2)
    ans.update(dict3)

    print("concatinated dict:",ans)
concatenate_dictionaries()

# output:
# dictionary 1:{'a': 121, 'b': 24}
# dictionary 2:{'c': 368, 'd': 440}
# dictionary 3:{'e': 505, 'f': 68}
# concatinated dict:{'a': 121, 'b': 24, 'c': 368, 'd': 440, 'e': 505, 'f': 68}


# 2. Write a program to check whether a dictionary is empty or not.

def is_empty():
    dict = {}

    if not dict:
        print("dictionary is empty.")
    else:
        print("dictionary is not empty.")
is_empty()

# output:
# dictionary is empty.


#3. Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

def dep_minmax_salary():
    list = [{"dep":1,"roll":101,"salary":10000000},
        {"dep":1,"roll":102,"salary":5000000},
        {"dep":1,"roll":103,"salary":2000000},
        {"dep":2,"roll":104,"salary":12000000},
        {"dep":2,"roll":105,"salary":1000000},
        {"dep":2,"roll":105,"salary":16000000},
        ]
    salary = {}
    for i in list:
        if i["dep"] not in salary:
            salary[i["dep"]] = []
        salary[i["dep"]].append(i["salary"])
    print(salary)

    dep1_salary = salary[1]
    dep2_salary = salary[2]
    min_dep1 = min(dep1_salary)
    min_dep2 = min(dep2_salary)
    max_dep1 = max(dep1_salary)
    max_dep2 = max(dep2_salary)

    print("department 1: minimum salary =",min_dep1,"maximum salary=",max_dep1)
    print("department 2: minimum salary =",min_dep2,"maximum salary=",max_dep2)
dep_minmax_salary()

# output:
# {1: [10000000, 5000000, 2000000], 2: [12000000, 1000000, 16000000]}
# department 1: minimum salary = 2000000 maximum salary= 10000000
# department 2: minimum salary = 1000000 maximum salary= 16000000


#4. Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.

def character_freq():
    s = input("Enter a string:")
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    print("character frequency Dictionary:",freq)
# character_freq()

# output:
# Enter a string:hello
# character frequency Dictionary:{'h': 1, 'e': 1, 'l': 2, 'o': 1}


#5. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

def bill():
    prices={"rice": 50,"wheat": 40,"sugar": 30,"Milk": 60}
    quantities={"rice": 2,"wheat": 3,"sugar": 1,"Milk": 5}

    total = 0

    for i,q in quantities.items():
            total += prices[i]*q

    print("Total Grocery Bill:",total)
bill()

# output:
# Total Grocery Bill:550
