# A program to calculate the energy of an object at rest, with relativity.

print(" ")
Mass = int(input("Enter the body's mass\n"))

# Eienstien's law.
print("Eienstien law of energy: Energy = mass * speed of light squared\n")

speed_of_light = 1.079 ** 9                                                 # In km/s
speed_of_light2 = 299792458                                                 # In m/s

Energy = Mass * speed_of_light ** 2
Energy2 = Mass * speed_of_light2 ** 2

print("The Energy of the given object in terms of kilograms per second  is:  %s kg/s\n" % Energy)
print("The Energy of the given object in terms of grams per second  is:  %s g/s\n" % Energy2)

# Energy in terms of kg's is based on light speed in kilometres per second.
# Energy in terms of grams per second is based on light speed in metres per second.


