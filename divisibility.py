
# To find divisible numbers for 3.

divisors = []
my_num = 3

for i in range (1, 100):
    if my_num % i == 0:
        divisors.append(i)
        length = len(divisors)
        if length == 2:
            print(" %s is a prime" % my_num)

print(divisors)

