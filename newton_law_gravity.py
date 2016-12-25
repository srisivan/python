# A program to get the approximate value of newton's law.


print("This is a program to calcute the Force between two bodies, Using Newton's law of gravity.")



Gravitational_constant = 6.67 * 10 ** -11

print(" ")
Mass1 = int(input("Enter Mass of Body 1 \n"))
Mass2 = int(input("Enter Mass of Body 2\n"))

Distance = int(input("Enter distance between 2 bodies.\n"))



print("Newton's law: Force = Gravitational constant * (Mass1 * Mass2) / Distance squared\n")




print("You have entered:")
       
print("Mass of Body1 = %s" % Mass1 )
print("Mass of Body2 = %s" % Mass2 )

print("Distance between bodies = %s " %  Distance)

# Newtons's law.
Force = Gravitational_constant * ( Mass1 * Mass2) / Distance ** 2



# The 'e' in the result corresponds to power.
print("The approximate force between them is %s \n" % Force)

print("The 'e' corresponds to power.\n")




