# def flatten(nestedList):
#     # Write your code here
#     res = []
#     for i in nestedList:
#         if isinstance(i, list):
#             res += flatten(i)
#         else:
#             res.append(i)
#     return res

# print(flatten(  [4,[3,[2,[1]]]]  ))

# def minSum(nums):
# 	nums.sort(lambda x, y => -1 if int(str(x)+str(y))<int(str(y)+str(x)) else 1)
# 	return reduce(lambda x, y => str(x)+str(y), nums)

# print(minSum([1,2,3]))
from functools import cmp_to_key
a = [1, 2, 3]

def foo(a, b):
	return -1 if (a+b)%2 == 1 else 1

a.sort(key=cmp_to_key(foo))
print(a)


