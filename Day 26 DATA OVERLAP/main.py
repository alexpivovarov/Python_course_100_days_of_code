file_1 = open("file1.txt", "r")
list1 = file_1.readlines()

file_2 = open("file2.txt", "r")
list2 = file_2.readlines()

result = [int(num) for num in list1 if num in list2] # 1st "in" is used for looping. 2nd "in" is used for condition

print(result)
