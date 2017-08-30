def shape(A):
	num_rows = len(A)
	num_cols = len(A[0])
	return num_rows,num_cols

def get_row(A,i):
	return A[i]

def get_col(A,j):
	return [A_i[j] for A_i in A]


# entry_fn 用來生成矩陣元素的函式

def make_matrix(num_rows,num_cols,entry_fn):
	return [ [entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i,j):
	return 1 if i == j else 0 

def make_function(i,j):
	return i,j

A = [[1,2,3],
	 [4,5,6]]

B = [[1,2],
	 [3,4],
	 [5,6]]

print(shape(A))
print(get_row(A,0))
print(get_col(A,2))
# print(make_matrix(10,10,make_function))
print(make_matrix(5,5,is_diagonal))

