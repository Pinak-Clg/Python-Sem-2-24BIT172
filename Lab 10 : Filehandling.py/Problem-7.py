# 7. If an Employee object contains following details: 
# empcode, empname, Date of Joining, Salary 
# Write a program to serialize and deserialize this data.

import json

employee = {"empcode":101, "empname":"Pinak", "DateOfJoining":"2027-05-01", "Salary":50000000}

# serialization
with open('employee.json', 'w') as file:
    json.dump(employee, file)

# deserialization
with open('employee.json', 'r') as file:
    data = json.load(file)

print(data)

# {"empcode":101, "empname":"Pinak", "DateOfJoining":"2027-05-01", "Salary":50000000}

