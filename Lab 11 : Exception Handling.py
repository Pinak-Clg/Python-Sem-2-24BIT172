
# Problem:
# Write a program that receives an integer an input. If a string is entered instead of an integer, 
# then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied.

# Exception handling

while True:
    try:
        a = int(input("Enter a number:"))
        break
    except ValueError:
        print("Enter a number instead of a string")

# output:
# Enter a number:pinak
# Enter a number instead of a string
# Enter a number:vipulbhai
# Enter a number instead of a string
# Enter a number:thummar
# Enter a number instead of a string
# Enter a number:123
