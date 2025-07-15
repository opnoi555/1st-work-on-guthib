start = 60
limit = 130
step = 10
print("KPH\tMPH")
print("--------------")
for kph in range (start, limit + step, step):
    mph_result = kph * 0.6214
    print(kph,"\t",format(mph_result,"0.1f"))