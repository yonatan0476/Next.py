# 1.5

# 1
with open("names.txt", 'r') as file:
    print(max(file.read().split("\n"), key=len))

# 2
with open("names.txt", 'r') as file:
    print(sum([len(word) for word in file.read().split("\n")]))

# 3
with open("names.txt", 'r') as file:
    words_list = sorted(file.read().split("\n")[:-1], key=len)
print('\n'.join([name for name in words_list if len(name) == len(words_list[0])]))

# 4
with open("names.txt", 'r') as file:
    with open("name_length.txt", 'w') as new_file:
        new_file.write("\n".join([str(len(word)) for word in file.read().split("\n")[:-1]]))

# 5
length = int(input("Enter a number: "))
with open("names.txt", 'r') as file:
    print('\n'.join([name for name in file.read().split("\n")[:-1] if len(name) == length]))
