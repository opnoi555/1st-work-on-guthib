numbers = [4,2,9,1,5,6]

length = len(numbers)
print(f"Lenth of the list: {length}")

total_sum = sum(numbers)
print(f"Sum all of elements: {total_sum}")

max_value = max(numbers)
print(f"Maximum value: {max_value}")

min_value = min(numbers)
print(f"Minimun vaue: {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [False,True,False]
any_true = any(bool_list)
print(f"Is any element true?: {any_true}")

all_true = all(bool_list)
print(f"Are all element true?: {all_true}")

string = "hello"
char_list = list(string)
print(f"List of character : {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed list:{reversed_numbers}")

enumerated_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerated_numbers}")