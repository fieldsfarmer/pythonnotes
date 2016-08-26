#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello_world():
	print('Hello, world!')

def log(func):
	def wrapper(*args, **kw):
		print('Calling %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper

hello_world()

@log
def hello_dec():
	print('Hello, decorator!')

hello_dec()
print(hello_dec.__name__)     # wrapper

def log1(text):
	def dec(func):
		def wrapper(*args, **kw):
			print('%s %s():' %(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return dec

@log1('Let\'s do')
def hello_another_dec():
	print('Hello, another decorator!')

hello_another_dec()
print(hello_another_dec.__name__)    # wrapper


import functools

def log_better(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('Calling %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper

@log_better
def hello_third_dec():
	print('Hello, the third decorator!')

hello_third_dec()
print(hello_third_dec.__name__)   # hello_third_dec

def log1_better(text):
	def dec(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' %(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return dec

@log1_better('Execute:')
def hello_fourth_dec():
	print('Hello, the fourth decorator!')

hello_fourth_dec()
print(hello_fourth_dec.__name__)     #  hello_fourth_dec

def log_no_matter_args(s):
	def dec(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			ss = 'Calling'
			if isinstance(s, str):
				ss = s
			print('%s %s():' %(ss, func.__name__))
			return func(*args, **kw)
		return wrapper
	return dec if isinstance(s, str) else dec(s)

@log_no_matter_args
def hello_fifth_dec():
	print('Hello, the fifth decorator!')

hello_fifth_dec()
print(hello_fifth_dec.__name__)

@log_no_matter_args('Fuck')
def hello_fifth_dec():
	print('Hello, the fifth decorator!')

hello_fifth_dec()
print(hello_fifth_dec.__name__)


def loglog(text='call'):
    def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                    print('begin %s %s():' % (text,func.__name__))
                    v = func(*args,**kw)
                    print('end %s %s():' % (text,func.__name__))
                    return v
            return wrapper
    return loglog()(text) if hasattr(text,'__call__') else decorator

@loglog
def hello_sixth_dec():
	print('Hello, the sixth decorator!')

hello_sixth_dec()


@loglog('Try this:')
def hello_sixth_dec():
	print('Hello, the sixth decorator!')

hello_sixth_dec()



