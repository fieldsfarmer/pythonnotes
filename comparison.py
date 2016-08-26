from functools import cmp_to_key
a = [1, 2, 3]

def reverse_cmp(a, b):
	return b-a

# a.sort(key=cmp_to_key(reverse_cmp))  #python3 
a.sort(cmp=reverse_cmp)  #python 2
print(a)



def my_compare(a, b):
	s = str(a)+str(b)
	t = str(b)+str(a)
	if s<t:
		return -1
	elif s==t:
		return 0
	else:
		return 1

# arr = [3, 32, 321]
arr = [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,
97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,
85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,
61,28,26,78,28,28,16,1,56,31,47,85,27,30,
85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
arr.sort(key=cmp_to_key(my_compare))

print (''.join([str(i) for i in arr]))
