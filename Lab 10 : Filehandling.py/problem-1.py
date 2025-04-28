# 1. Write a program to create a csv file that we can directly open in MS-Excel.
import csv
def create_csv():
    with open('students.csv', 'w') as file:
        w = csv.writer(file)
        w.writerow(["RollNo", "Name", "Subject1", "Subject2", "Subject3"])
        w.writerow([1,"Pinak", 95, 100, 99])
        w.writerow([2,"Roshan",98, 92, 99])
    print("CSV file created successfully.")
create_csv()
# Output:
# CSV file created successfully.
# Excel File is created
