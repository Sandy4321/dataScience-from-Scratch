def magic(*args, **kwargs):
	print('unnamed args:',args)
	print('keyword args:',kwargs)


magic(1,2,key="word",key2="word2")

def double_correct(f):
	def g(*args,**kwargs):
		return 2 * f(*args,**kwargs)
	return g 

def f2(x,y):
	return x+y

g = double_correct(f2)
print(g(1,2))