import random
import string

sentence = input("sentence: ")
space = ""

for word in sentence:
    space += word + random.choice(string.ascii_letters)
print(space)