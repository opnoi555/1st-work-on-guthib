inchar = input("input your character: ")
if inchar >= "A" and inchar <=  "Z":
    print("you input Uppercase Letter ", inchar)
elif inchar >= "a" and inchar <= "z":
    print("you input Lowercase Letter ", inchar)
elif inchar >= '0' and inchar <= "9":
    print("you input Number", inchar)
else:
    print("it's not a letter or number", inchar)