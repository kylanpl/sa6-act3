strings = ["yo", "salutations", "hola", "hello", "greetings", "howdy", "hi"]
strings_sorted = sorted(strings, key=lambda x : (len(x), x))

print(strings_sorted)