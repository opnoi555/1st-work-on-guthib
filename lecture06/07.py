fruit_with_deplicates = ["apple","banana","apple","cherry","apple","kiwi"]
while "apple" in fruit_with_deplicates:
    fruit_with_deplicates.remove("apple")
print(f"Fruit after remove: {fruit_with_deplicates}")