
print("Please enter your weight in kg.")
weight = input("WEIGHT in KG :   ")

print("\n")


print("Please enter your height in metres.")
h = input("HEIGHT in METRES:  ")

bmi = weight / (h * h)
BMI = round(bmi, 2)
weight_i = (24 * (h * h))

print("You are %s BMI" % BMI)

if bmi < 18.5:
    print("Your BMI is %s, and this means that you could possibly be a underweight, and malnourished." % BMI)
    weight_to_be_increased = weight_i - weight
    print("You are underweight, and that's not good. to have a normal BMI, you must at least increase your weight by %s kilos." % round(weight_to_be_increased,1)) 

elif bmi == 18.5 or bmi < 24.9:
    print("Your BMI is %s, this means that you are in healty range for young and middle - aged adults." % BMI)

elif bmi == 25.0 or bmi < 29.9:
    print("Your BMI is %s, this says that you are considered as overweight." % BMI)
    weight_to_be_reduced = weight - weight_i
    print("You are overweight. To be of normal BMI, you should reduce your weight by %s kilos." % round(weight_to_be_reduced,1))

elif bmi > 30:
    print("Your BMI is %s, this says that you are obese." % BMI)
    weight_to_be_decreased = weight - weight_i
    print("You are obese. To be a normal BMI, you must reduce your weight by %s kilos." % round(weight_to_be_decreased,1))

