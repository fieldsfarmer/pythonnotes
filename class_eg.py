#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def print_info(self):
		print('%s is %d' %(self.name, self.age))

xiaoming = Student('Xiaoming', 12)

print(xiaoming.name, xiaoming.age)
xiaoming.print_info()

class Student2():
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	def print_info(self):
		print('%s, %d' %(self.__name, self.__age))

xiaohong = Student2('Xiaohong', 11)
xiaohong.print_info()

class Animal():
	def run(self):
		print('Animal is running')

class Cat(Animal):
	def run(self):
		print('Cat is running')

class Dog(Animal):
	def run(self):
		print('Dog is running')

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Cat())
run_twice(Dog())

class Timer():
	def run(self):
		print('Start...')

run_twice(Timer())

class Class_with_slot():
	__slots__ = ('name', 'age')

class_with_slot = Class_with_slot()
class_with_slot.name = 'nima'
class_with_slot.age = 12

# class_with_slot.score = 99 ## You cannot do this in python3

# print('%s, %d' %(class_with_slot.name, class_with_slot.age))
# #the following works in python 2.7
# print('%s, %d, %d' %(class_with_slot.name, class_with_slot.age, class_with_slot.score))

### use of property
### the following birth can be read and written; while age can only be read
class Student_using_property():
	@property
	def birth(self):
		return self.__birth
	@birth.setter
	def birth(self, v):
		self.__birth = v
	@property
	def age(self):
		return 2016 - self.__birth
# It does not work in python 2.7
s = Student_using_property()
s.birth = 1990
print('%d, %d' %(s.birth, s.age))
s.birth = 1900
print('%d, %d' %(s.birth, s.age))


#### customization
class Chain():
	def __init__(self, path=''):
		self.__path = path
	def __getattr__(self, path):
		return Chain('%s/%s' %(self.__path, path))
	def __str__(self):
		return self.__path
	__repr__ = __str__

a = Chain()
b = a.status.user.timeline.list

print(a)
print(b)


##### implement __iter__ and __getitem__
class Fib():
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 500:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		### simple version
		# a, b = 1, 1
		# for i in range(n):
		# 	a, b = b, a+b
		# return a
		if isinstance(n, int):
			a, b = 1, 1
			for i in range(n):
				a, b = b, a+b
			return a
		if isinstance(n, slice):
			s = n.start
			e = n.stop
			if s is None:
				s = 0
			a, b = 1, 1
			L = []
			for i in range(e):
				if i >= s:
					L.append(a)
				a, b = b, a+b
			return L


for n in Fib():
	print(n)

f = Fib()
print(f[10])


print(f[1:11])

print(f[:11])

