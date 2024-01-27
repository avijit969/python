height = float(input("enter your height in meter"))
weight = float(input("enter your wight in kg"))
BMI = round(weight / (height ** 2))
if BMI < 18.5:
    print(f"your BMI is {BMI} and you are underweight.")
elif BMI < 25:
    print(f"your BMI is {BMI} and you have a normal weight.")
elif BMI < 30:
    print(f"your BMI is {BMI} and you are overweight.")
elif BMI < 35:
    print(f"your BMI is {BMI} and you are obese.")
else:
    print(f"your BMI is {BMI} and you are clinically obese.")
