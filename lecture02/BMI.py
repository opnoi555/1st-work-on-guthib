weight = float(input("Enter your weight : "))
height = int(input("Enter your height : "))
height_in_meter = float(height / 100)
bmi = float(weight / (height_in_meter * height_in_meter))
print("your BMI is ", format(bmi, "0.2f"))
if bmi <= 18.5 :
    print("You are under weight")
elif bmi >= 18.5 and bmi <= 24.9 :
    print("you are normal")
elif bmi >= 25 and bmi <= 29.9 :
    print("you are over weight")
elif bmi >= 30 and bmi <= 34.9 :
    print("you are obese")
else:
    print("you are extremely obese")