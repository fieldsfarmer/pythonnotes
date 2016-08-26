# import os

# print('process (%s) starts ...' %(os.getpid()))

# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent process is (%s)' %(os.getpid(), os.getppid()))
# else:
# 	print ('I am process (%s) and just created (%s)' %(os.getpid(), pid))

#################################

# import os
# from multiprocessing import Process

# def run_proc(name):
# 	print('Run child process %s (%s)' %(name, os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process (%s).' %(os.getpid()))
# 	p = Process(target=run_proc, args=('test', ))
# 	print('Child process will start ...')
# 	p.start()
# 	p.join()
# 	print('Child process ends ...')

#################################

import os, time, random
from multiprocessing import Pool

def long_time_task(name):
	print('Run task %s (%s) ... ' %(name, os.getpid()))
	start = time.time()
	time.sleep(3*random.random())
	end = time.time()
	print('Task %s runs %0.2f seconds' %(name, end - start))

if __name__ == '__main__':
	print('Parent process (%s).' %(os.getpid()))
	p = Pool(5)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting all subprocesses done ...')
	p.close()
	p.join()
	print('All subprocesses done ...')



