# q1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
largest_number = max(lst)
print(largest_number)
lst.remove(min(lst))
lst.sort()
last_4_numbers = lst[-4:]
print(last_4_numbers)

# q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
count_python = sum(1 for sublist in main_lst if isinstance(sublist[0], str) and sublist[0] == "python")
print("Number of times 'python' is repeated within sublists:", count_python)
# q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
sentence = ' '.join(word.capitalize() for word in my_lst)
print("Output:", sentence)

# q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst = my_lst[:]
print("Original list:", my_lst)
print("new list:", new_lst)

# q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2] = my_lst[4]
print("Output:", my_lst)

# q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum_nums = sum(nums)
print("Output:", sum_nums)

# q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple_1= tuple1 + (9,)
print("Output:", tuple_1)

# q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
joined_tuple = tuple1 + (9,) + tuple2
print("Output:", joined_tuple)



