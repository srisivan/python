
maximum_length = int(input("Enter : "))

for i in range(0, maximum_length):
    print("#" * i)

for j in range(1, maximum_length):
    minimum_length = maximum_length - j
    print("#" * minimum_length)
