#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def foo(a, b):
	try:
		print('Try ... ')
		r = float(a)/int(b)
		print('Result:', r)
	except ValueError as e:
		print('ValueError:', e)
	except ZeroDivisionError as e:
		print('ZeroDivisionError:', e)
	except BaseException as e:
		print('BaseException:', e)
	else:
		print('No error!')
	finally:
		print('Finally ... ')
	print('END')

foo('a', 1)
foo('1', 0)
foo('1', '2')