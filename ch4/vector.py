import functools,math


def vector_add(v,w):
	return [v_i+w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
	return [v_i+w_i for v_i, w_i in zip(v,w)]

def dot(v,w):
	return sum(v_i*w_i for v_i, w_i in zip(v,w))

def squared_distance(v,w):
	return sum_of_squares(vector_subtract(v,w))

def distance (v,w):
	return magnitude(vector_subtract(v,w))

# def vector_sum(vectors):
# 	result = vectors[0]
# 	for vector in vector[1:]
# 		result = vector_add(vector,result)

def vector_sum(vectors):
	return functools.reduce(vector_add,vectors)

def scalar_multifply(c,v):
	return [c * v_i for v_i in v]

# 算所有vectorList的平均
def vector_mean(vectors):
	n = len(vectors)
	return scalar_multifply(1/n,vector_sum(vectors))

def sum_of_squares(v):
	return dot(v,v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))






vector = [[1,2,3],[2,3,5]]
v1 = [1,2,3]
v2 = [3,4,1]

print(vector_sum(vector))
 print(magnitude(v1))
print(distance(v1,v2))
