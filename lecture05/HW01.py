def format_strings(*word_sended):
    word = "".join(word_sended)
    return word.upper()

result = format_strings("Hello", "world","this","is","a","test")
print(result)

result = format_strings("Python","is","fun")
print(result)

result = format_strings("Concatenate","these","strings","please")
print(result)