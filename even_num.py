# Program to print only Even numbers for the given range

# What is even number?
#    - A number divisible by two is called even number (What this means is Reminder is Zero)
#
# reminder = (i % 2)
# if (reminder == 0
# 
#
# What components of Python is used?
# - input function
# - Modulo (%)
# - Interger data type
# - For Loop
# - If conditon
# - Print function
# 
# Committed to Version Control



range_val = (int)(input("Enter the required Range\n"))


for i in range(1, range_val):
	if ((i % 2) == 0):
		print (i)


range_val_start = (int)(input("Enter the start range\n"))
range_val_end = (int)(input("Enter the end range\n"))



for i in range(range_val_start, range_val_end):
	if ((i % 2) == 0):
		print (i)
