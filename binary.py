# A program to convert inputs into ASCII and binary form #

name = input("Enter : ")
for c in name:
	print(c, "in ASCII table:", ord(c), "in binary form:", bin(ord(c)))
