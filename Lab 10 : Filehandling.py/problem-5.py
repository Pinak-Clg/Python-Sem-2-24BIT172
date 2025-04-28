# 5) Copy contents from one file to another converting lowercase to uppercase.
def copy_and_uppercase():
    with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
        for line in f1:
            f2.write(line.upper())
    print("Done.")
copy_and_uppercase()
# Output:
# Done (File copied with uppercase)
# (output.txt will have all content in UPPERCASE)
