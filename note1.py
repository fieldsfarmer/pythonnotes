class A:
	pass

class B:
	def show(self):
		print 'I am B'

A.__bases__ = (B,)
a = A()
a.show()

# This book is on how to use C to implement Python
print ('python version: ', python_version())