phonebook = {"Phoorin":"0629534488"
             ,"Rin":"65685282"
             ,"Bana":"8798989"}

print(phonebook)

print(phonebook["Rin"])
print(phonebook.get("Bana"))

key = "Pluto"
if key in phonebook:
    print(phonebook["Pluto"])
else:
    print(key + "not in phonebook")

phonebook["Simson"] = "777-4567"
phonebook["Pluto"] = "777-4444"
phonebook["Mickey"] = "777-2122"
print(phonebook)

del phonebook["Simson"]
print(phonebook)