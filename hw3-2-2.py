# Author JRI 10/6/21

height = int(input("Insert your height in meters "))
weight = int(input("Insert your weight in kilograms "))

bmi = weight / height ** 2

if int(bmi) > 40:
    print("You are extremely obese!")
elif int(bmi) > 30:
    print("You are obese!")
elif int(bmi) > 25:
    print("You are overweight!")
elif int(bmi) > 19:
    print("You are healthy!")
else:
    print("You are underweight!")
