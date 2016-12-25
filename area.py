import math

# Function to calculate area of triangle"
def area_of_a_traingle(b,h):
	"""Find area of Triangle"""
	area = (0.5 * b * h)
	print(area)
	return area

# Function to calculate area of circle"
def area_of_a_circle(r):
	"""find area of circle"""
	area = ( math.pi * r * r)
	print(area)
	return(area)


# Function to calculate area of rectangle"
def area_of_a_rectangle(l,b):
	"""find the area of rectangle"""
	area = l * b
	print(area)
	return(area)


print("To get the area of a circle")
radius = int(input("enter radius: "))
area_of_a_circle(radius)

print("To get the area of a traingle.") 
length = int(input("enter length of triangle: "))
base = int(input("enter base of triangle: "))
area_of_a_traingle(length, base);

print("To get the area of a rectangle.")
length = int(input("enter length of rectangle: "))
height = int(input("enter height  of rectangle: "))
area_of_a_rectangle(length, height)
