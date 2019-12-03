#更多的条件测试
name1 = 'Tom'
name2 = 'Tom'
name3 = 'tom'
print("name1 = name2:", name1 == name2)
print("name1 = name3:", name1 == name3)
#lower()函数
print("name1.lower() = name3.lower():", name1.lower() == name3.lower())

num1 = 19
num2 = 20
print('\nnum1 = num2:', num1 == num2)
print('num1 > num2:', num1 > num2)
print('num1 < num2:', num1 < num2)
print('num1 >= num2:', num1 >= num2)
print('num1 <= num2:', num1 <= num2)
#and or
print('True or False:', num1 == num2 and num1 < num2)
print('True or False:', num1 != num2 and num1 <num2)
print('True or False:', num1 == num2 or num1 < num2)

name = ['Tom', 'Terry', 'Mask']
print('True or False:', 'Tom' in name)
print('True or False:', 'tom' not in name)