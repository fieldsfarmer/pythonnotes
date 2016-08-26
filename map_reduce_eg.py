#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from functools import reduce

# # change string to float number
# def char2num(c):
# 	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]

# def str2float(s):
# 	if '.' in s:
# 		ss = s.replace('.','')
# 		return float(reduce(lambda x, y: x*10+y, map(char2num, ss))/(10**(len(s)-s.index('.')-1)))
# 	else:
# 		return reduce(lambda x, y: x*10+y, map(char2num, s))

# print(str2float('1230.456789'))
# print(str2float('1234567890'))

