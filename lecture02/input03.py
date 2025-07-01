name = input("what am gonna call you? : ")
print("So you are : ", name)

age = int(input("you know this is a night club what your age? : "))
if age >= 18 :
    print("So you are over 18")
    income = float(input("i dont know but my boss told me to ask for the income for some reason : "))
    print("So your income is ", format(income, "12.2f") ," Thank for that information, here you go")
else:
    print ("get out of here!!!")