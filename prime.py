#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Must run by python3
'''
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

def _not_divisible(n):
	return lambda x: x%n > 0

def prime():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		# print n
		yield n
		it = filter(_not_divisible(n), it)

for n in prime():
	if n < 100:
		print (n)
	else:
		break






