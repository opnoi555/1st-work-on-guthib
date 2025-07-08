employees = int(input("Number of employees: "))
if employees < 50:
    print("Small company")
elif employees < 250:
    print("Mediun company")
elif employees >= 250:
    print("Large company")