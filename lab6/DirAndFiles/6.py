import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'x'):
        pass