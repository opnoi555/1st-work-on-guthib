string01 = "Mary"
string02 = "Mark"

if string01 == string02:
    print(f'"{string01}" and "{string02}" are equal')
else:
    print(f'"{string01}" and "{string02}" are not equal')

if string01 < string02:
    print(f'"{string01}" come before "{string02}" in lexicographical order')
elif string01 > string02:
    print(f'"{string01}" come after "{string02}" in lexicographical order')

if string01.lower() == string02.lower():
    print(f'"{string01}" and "{string02}" are equal when case is ignored')
else:
    print(f'"{string01}" and "{string02}" are not equal when case is ignored')