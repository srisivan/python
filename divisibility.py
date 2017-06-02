
# To find divisible numbers for 3.

divisors = []
my_num = int(input("Enter the desired number : "))

for i in range (1, (my_num + 1)):
    if my_num % i == 0:
        divisors.append(i)
        length = len(divisors)

if length == 2:
    print("%s is a prime number" % my_num)
else:
    print("%s is a composite number" % my_num)

print(divisors)
print("The number of divisors is %s" % length)
