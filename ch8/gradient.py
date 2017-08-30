import functools
from functools import partial
import matplotlib.pyplot as plt
import random,math


# vector method

def vector_subtract(v,w):
	return [v_i+w_i for v_i, w_i in zip(v,w)]

def dot(v,w):
	return sum(v_i*w_i for v_i, w_i in zip(v,w))

def distance (v,w):
	return magnitude(vector_subtract(v,w))

def sum_of_square(v):
	return dot(v,v)

def magnitude(v):
	return math.sqrt(sum_of_square(v))

def scalar_multifply(c,v):
	return [c * v_i for v_i in v]

# ======================================

def sum_of_squares(v):
	return sum(v_i**2 for v_i in v)

def difference_quotient(f,x,h):
	return (f(x+h)-f(x))/h

def square(x):
	return x*x

def derivative(x):
	return 2*x


def plot_estimate_derivative () :
	derivative_estimate = partial(difference_quotient,square,h=0.001)
	x = range(-10,10)
	plt.title('Actual Derivative vs. Estimates')
	plt.plot(x, list(map(derivative,x)) , 'rx' , label='Actual')
	plt.plot(x, list(map(derivative_estimate,x)) , 'b+' , label='Estimate')
	plt.legend(loc=9)
	plt.show()
def partial_difference_quotient(f,v,i,h):
	w = [ v_j +(h if j ==i else 0) for j,v_j in enumerate(v)]
	return (f(w)-f(v))/h

# 缺點 => 計算太久

def estimate_gradient(f,v,h = 0.001):
	return [partial_difference_quotient(f,v,i,h)
			for i,_ in enumerate(v)] # i代表你要偏微分的變數

def step(v,direction,step_size):
	return [v_i + direction_i * step_size for v_i,direction_i in zip(v,direction)]

def sum_of_squares_gradient(v): # x^2 微分變 2*x
	return [ 2 * v_i for v_i in v ]

def gradient_dessent_sum_of_square():
	v = [random.randint(-10,10) for i in range(3)]
	tolerance = 0.01
	while True:
		gradient = sum_of_squares_gradient(v)
		next_v = step(v,gradient,-0.01) # 沿著梯度的反方向，可得到LocalMinimum
		if distance(next_v,v) < tolerance:
			print(next_v)
			break
		v = next_v

def safe(f):
	def safe_f(*args,**kwargs):
		try:
			return f(*args,**kwargs)
		except:
			return float('inf') # 回傳無限大
	return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes target function"""

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0                           # set theta to initial value
    target_fn = safe(target_fn)               # safe version of target_fn
    value = target_fn(theta)                  # value we're minimizing

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]

        # min(變數,key=函式名稱) 把變數代進函式找最小值
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)

def in_random_order(data):
	indexs = [ i for i,_ in enumerate(data)]
	random.shuffle(indexs)
	print(indexs)
	for i in indexs:
		yield data[i]

def minimize_stochastic(target_fn,gradient_fn,x,y,theta_0,alpha_0=0.001):
	data = zip(x,y)
	theta = theta_0
	alpha = alpha_0
	min_theta,min_value = None,float('inf')
	iteration_with_no_improvement = 0

	while iteration_with_no_improvement <100: #如果進行了100迭代仍毫無進展，則停下來
		value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )
		if value < min_value:
			min_theta,min_value = theta,value
			iteration_with_no_improvement = 0
			alpha = alpha_0
		else:
			iteration_with_no_improvement += 1
			alpha *= 0.9

		for x_i,y_i in in_random_order(data):
			gradient_i = gradient_fn(x_i,y_i,theta)
			theta = vector_subtract(theta,scalar_multifply(alpha,gradient_i))
			
	return min_theta



def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn),
                               negate_all(gradient_fn),
                               x, y, theta_0, alpha_0)





# plot_estimate_derivative()
# gradient_dessent_sum_of_square()
v = [random.randint(-10,10) for i in range(3)]
v = minimize_batch(sum_of_squares, sum_of_squares_gradient, v)
print(v)
# data = in_random_order([5,2,4])
# for i in data:
# 	print(i)


