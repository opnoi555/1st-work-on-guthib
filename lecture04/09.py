input_sudcoon = int(input("ใส่แม่สูตรคูณที่ต้องการไอ่น้อง : "))
input_num_limit = int(input("อยากให้คูณถึงเลขเท่าไหร่ : "))
print("เลขที่คูณ\tผลลัพธ์")
for coon_numbers in range (1,(input_num_limit + 1)):
    numb_result = input_sudcoon * coon_numbers
    print(coon_numbers, "\t", numb_result)