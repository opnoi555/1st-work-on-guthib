phonebook = {"Phoorin":"0629534488"
             ,"Rin":"65685282"
             ,"Bana":"8798989"
             ,"Dorontabi":"512874586loe"}

heroesdict = {}
heroesdict["Hulk"] = "888-1111"
heroesdict["Ironman"] = "888-2222"
print(heroesdict.get("Halk","Key not found"))
print(heroesdict.get("Hulk","Key not found"))

for key , value in phonebook.items():
    print(key,value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop("Banakun","Element not found"))
print(phonebook.pop("Bana","Element not found"))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print("after clear")
print(phonebook)