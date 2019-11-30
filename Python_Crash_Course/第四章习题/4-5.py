#计算1~1000000总和
import time
numbers =range(1, 1000001)
print(min(numbers))
print(max(numbers))
tic = time.time()
a = sum(numbers)
toc = time.time()
print(a, '\n程序执行' + str(toc - tic) + 's' )