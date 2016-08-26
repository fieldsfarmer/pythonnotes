#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_not_working():
	f = []
	for i in range(1, 4):
		def ff():
			return i*i
		f.append(ff)
	return f

f1, f2, f3 = count_not_working()

print(f1(), f2(), f3())                  # (9, 9, 9)

def count_long_but_works():
	def ff(i):
		def g():
			return i*i
		return g
	f = []
	for i in range(1, 4):
		f.append(ff(i))
	return f

g1, g2, g3 = count_long_but_works()

print(g1(), g2(), g3())                   # (1, 4, 9)

def count_using_lambda():
	def ff(i):
		return lambda: i*i
	f = []
	for i in range(1, 4):
		f.append(ff(i))
	return f

h1, h2, h3 = count_using_lambda()
print(h1(), h2(), h3())                   # (1, 4, 9)


