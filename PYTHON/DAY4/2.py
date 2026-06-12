## find maximum number in a list

number = [3, 5, 7, 2, 8, 1]
max_num = number[0] ## we can also use max_num = float('-inf') to find the maximum number in the list
for i in number:
    if i > max_num:
        max_num = i
print(max_num)