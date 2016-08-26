import os
### s is the string of filename, d is the relative directory
def findStInFilename(s, d):
	for f in os.listdir(d):
		# print('123   ', f)
		curfile = os.path.join(d, f)
		# print(curfile)
		if s == f:
			if os.path.isfile(curfile):
				print('Filename: %s, Relation path: %s' %(s, curfile))
		if os.path.isdir(curfile):
			# print('here')
			findStInFilename(s, curfile)

findStInFilename('file_eg.py', '.')