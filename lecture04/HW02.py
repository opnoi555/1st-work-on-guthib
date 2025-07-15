max_col = int(input("Input your columns :"))
num_start = 1

while num_start <= 100:
    for _ in range(max_col):
        if num_start <= 100:
            print(num_start,"\t", end="")
            num_start += 1
        else:
            break
    print()

