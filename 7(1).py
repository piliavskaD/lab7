sentence = input("sentence: ")

lst = []
for word in sentence:
    lst.append(word)
    if word.isdigit():
        print(f"Index of numbers in sentence: {lst.index(word)}")

for del_elem in lst:
    if not del_elem.isdigit():
        print(del_elem)