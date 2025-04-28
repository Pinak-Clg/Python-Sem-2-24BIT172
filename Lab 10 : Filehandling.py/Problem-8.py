# 8. Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and 
# replacing each one of them with a blank space. 
ith open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:    
        for line in f1:
            words = line.split()
            edit = [word for word in words if word.lower() not in ('a', 'an', 'the')]
            f2.write(" ".join(edit) + '\n')
print("New file created without articles.")
