# Simple BMI Calculator 
# Tells if a person is overweight or not based on height & weight. 

name = "this person"
height_m = 1.65
weight_kg = 51

bmi = (weight_kg / height_m ** 2)
print("bmi")
if bmi < 25:
    print(name)
    print("is not overweight")
else: 
    print(name)
    print("is overweight")

