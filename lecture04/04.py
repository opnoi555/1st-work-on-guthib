input_string = str(input("Enter a string : "))
modified_string = ""
vowels = "aeiouAEIOU"

for char in input_string:
    if char in vowels:
        modified_string += "*"
    else:
        modified_string += char

print("Modidied string : ", modified_string)