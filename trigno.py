
Hyp_value = int(input("Please enter the hypotenuse value :    "))
Opp_value = int(input("Please enter the opposite value :  "))
Adj_value = int(input("Please enter the adjacent value :  "))

Tri = input(print("Do you need the value of sin or cos or tan? enter s for (sin),c for (cos) or t for (tan)."))

if (Tri == 's'):
	print("sin(opposite / hypotenuse)")
	print(Opp_value / Hyp_value)

elif (Tri == 'c'):
	print("cos(adjacent / hypotenuse)")
	print(Adj_value / Hyp_value)

elif (Tri == 't'):
	print("tan(opposite / adjacent)")
	print(Opp_value / Adj_value)

else:
	print("invalid entry(s,c,t)")



