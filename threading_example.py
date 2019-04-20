import threading 
import time
def sqr(num):
	global count
	print("Inside sqr func")
	# time.sleep(5)
	# print(num * num)
	lock.acquire()
	lock.acquire()
	for value in range(5):
		count+=5
		print(count)
		time.sleep(2)
	lock.release()
	lock.release()

def multiply(num1,num2):
	global count 
	print("Inside multiply function")
	# print(num1*num2)
	lock.acquire()
	for value in range(5):
		count+=2
		print(count)
		time.sleep(1)
	lock.release()

lock = threading.RLock()
count = 100
t1 = threading.Thread(target= sqr,args =(10,))
t2 = threading.Thread(target = multiply, args =(5,6))

t1.start()
# t1.join()
t2.start()
# Process => python 
# t1 => some code
# t2 => some code 

# Concurrent execution => 1 cpu with multiple cores 

# Non daemon => process will wait for this thread to finish the execution  
# Deamon => if all non deamon threads has finished the execution or not if yest terminate the process

# 1 Race condition 
# 2 Deadlock 
