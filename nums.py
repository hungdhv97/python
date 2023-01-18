import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rv = func(*args, **kwargs)
		total = time.time() - start
		print("Time: ", total)
		return rv

	return wrapper


def checker(func):
	def wrapper(*args, **kwargs):
		print('start')
		func(*args, **kwargs)
		print("end")

	return wrapper

@checker
@timer
def test():
	for _ in range(1000000):
		pass

test()