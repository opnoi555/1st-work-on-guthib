global_variable = "I'm outside function"

def my_func():
    print(global_variable)

my_func()

print(global_variable)