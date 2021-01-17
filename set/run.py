result = []
number_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# EX 1
for number in number_list:
    if not number in result:
        result.append(number)
print(result)

# EX 2
print(list(set(number_list)))