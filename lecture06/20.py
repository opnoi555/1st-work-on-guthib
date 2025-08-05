NUM_employees = 6

def main() :
    hour = [0] * NUM_employees

    for INDEX in range(NUM_employees):
        print("Enter the hour worked by employee ",\
              INDEX+1,": ",sep="",end="")
        hour[INDEX] = float(input())

    pay_rate = float(input("Enter the hourly pay rate: "))

    for INDEX in range(NUM_employees):
        gross_pay =hour[INDEX] * pay_rate
        print("Gross pay for employee ",INDEX+1,": $",\
            format(gross_pay,",.2f"),sep="")
        
main()