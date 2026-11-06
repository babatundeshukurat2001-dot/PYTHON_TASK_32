fruit = {"mango", "orange", "banana", "kiwi"}
name = ["opeyemi", "ola" , "mide", "tolu"]

fruit_dict = {word: name[index] for index, word in enumerate(fruit)}

print(fruit_dict)

