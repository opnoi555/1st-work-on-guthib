def is_armstrong(number):
    str_num = str(number)
    num_digits = len(str_num)
    total = 0

    for digit in str_num:
        total += int(digit) ** num_digits

    return total == number

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
