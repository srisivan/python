

record = []

name = raw_input("Enter your name : ")
record.append(name)

standard = raw_input("Enter the standard : ")
record.append(standard)

email = raw_input("Enter the email address : ")
record.append(email)

number = raw_input("Enter your phone number : ")
record.append(number)

name, standard, email, number = record

print("Do you want your details to be displayed? [Yes or No]")
answer = raw_input()

if answer == "yes" or "Yes":
    print("Name : %s " % name)
    print("standard : %s " % standard)
    print("email : %s" % email)
    print("Phone number : %s" % number)
else:
    print("Okay, your details have been stored.")
