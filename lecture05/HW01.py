"""
def format_strings(*word_sended):
    word = "".join(word_sended)
    return word.upper()

result = format_strings("Hello", "world","this","is","a","test")
print(result)

result = format_strings("Python","is","fun")
print(result)

result = format_strings("Concatenate","these","strings","please")
print(result)
"""
def format_strings(*args):
    word = "".join(args)
    return word.replace(" ","-").upper()
    # Your implementation here
    pass

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"