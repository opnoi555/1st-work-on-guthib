keep_going = "Y"

while keep_going == "Y":
    sale = float(input("Enter the amount of sales : "))
    comm_rate = float(input("Commission rate : "))

    commission = sale * comm_rate

    print(f'the commission is ${commission:.2f}')
    keep_going = input("Do you want to calculate another0" + \
                       "commission (Enter y for yes) : ").upper()
else:
    print("End")