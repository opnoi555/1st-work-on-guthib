work_hour = float(input("Your work hour : "))
hourly_pay_rate = float(input("Your hourly pay rate : "))
if work_hour > 40 :
    overtime = work_hour - 40
    pay = format((overtime * hourly_pay_rate * 1.5) + (40 * hourly_pay_rate), "0.2f")
else:
    pay = format(work_hour * hourly_pay_rate , "0.2f")
print("Your gross pay is", pay)