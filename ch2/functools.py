import functools
from functools import partial

def exp(base,power):
	return base**power

two_to_the = partial(exp,2) # partial(函數名稱,要代入的的第一個參數)
print(two_to_the(3))

square_of = partial(exp,power = 2 ) # 指定變數
print(square_of(2))



def double(x):
	return 2 * x

xs = [1,2,3,4]
twice_xs0 = [double(x) for x in xs]
print(twice_xs0)
print("===========================")

# map => 把函數用在多個元素（list、 set、dict）

twice_xs1 = map(double,xs)
for i in twice_xs1:
	print(i)

print("===========================")

list_doubler = partial(map,double)

twice_xs2 = list_doubler(xs)
for i in twice_xs2:
	print(i)

def multiply(x,y): return x*y

print("===========================")

products = map(multiply,[4,5],[1,2])

for i in products:
	print(i)

# functools.reduce => 會先計算1,2元素，再將1,2元素的結合與3元素作運算，以此類推

x_product = functools.reduce(multiply, xs)
list_product = partial(functools.reduce,multiply)
print(x_product)
print(list_product(xs))







