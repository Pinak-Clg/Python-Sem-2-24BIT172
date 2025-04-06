# 1) Count how many vowels are there in a string.Accept the string from the user.
def count_vowels():
    s = input("Enter a string:")
    count =0
    for ch in s:
        if ch in "aeiouAEIOU":
            count +=1
    print("Number of vowels:",count)
count_vowels()

# Output:
# Enter a string: Hello World
# Number of vowels:3

# 2.Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.
def convert_cases():
    s = input("Enter a string: ")
    
    lower= ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            lower+= chr(ord(ch) + 32)
        else:
            lower+= ch
    print("Lower case:",lower)

    upper= ""
    for ch in s:
        if 'a' <= ch <= 'z':
            upper += chr(ord(ch)-32)
        else:
            upper += ch
    print("Upper case:",upper)

    toggle = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            toggle+= chr(ord(ch)-32)
        elif 'A' <= ch <= 'Z':
            toggle += chr(ord(ch)+32)
        else:
            toggle += ch
    print("Toggle case:",toggle)
convert_cases()

# Output:
# Enter a string: Hello123
# Lower case:hello123
# Upper case:HELLO123
# Toggle case:hELLO123

# 3.Accept two strings. Check whether one string is there in another string.

def check_substring():
    s1 = input("Enter first string:")
    s2 = input("Enter second string:")
    if s2 in s1:
        print("substring found")
    else:
        print("substring not found")
check_substring()

# Output:
# Enter first string: HelloWorld
# Enter second string: World
# Substring found

# 4) Write a function that removes one string from another string, if present.
def remove_substring():
    main =input("Enter main string:")
    remove=input("Enter string to remove:")
    ans=main.replace(remove,"")
    print("Final string:",ans)

remove_substring()

# Output:
# Enter main string: abcdef
# Enter string to remove: cd
# Final string:abef



