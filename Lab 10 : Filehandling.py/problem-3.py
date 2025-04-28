# 3. Accept contact details from the user and create a vcard that we can directly store in our mobile.
def create_vcard():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    with open('contact.vcf', 'w') as file:
        file.write("BEGIN:VCARD\n")
        file.write("VERSION:3.0\n")
        file.write("N:",name,"\n")
        file.write("TEL:",phone,"\n")
        file.write("EMAIL:",email,"\n")
        file.write("END:VCARD\n")
    print("vCard created successfully")
create_vcard()

# Output:
# Enter name: Pinak
# Enter phone number: 999999999
# Enter email: xyz@gmail.com
# vCard created successfully.
