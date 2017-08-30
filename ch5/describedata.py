from collections import Counter
from matplotlib import pyplot as plt
import functools
import math


# vector method

def dot(v,w):
	return sum(v_i*w_i for v_i, w_i in zip(v,w))	

def sum_of_squares(v):
	return dot(v,v)



# ============================================

# 平均

def mean(v):
	return sum(v)/len(v)

# 中位數
def median(v):
	n = len(v)
	v_sorted = sorted(v)
	midpoint = n//2 # // 除法只取整數 
	if n % 2 == 1:
		return v_sorted[midpoint]
	else : 
		lo = v_sorted[midpoint]
		hi = v_sorted[midpoint-1]
		return (lo+hi)/2
# 百分位數 => p介在0-1間表示要處在多少%的資料
def quantile(v,p):
	p_index = int( p * len(v))
	v_sorted = sorted(v)
	return v_sorted[p_index]


# 眾數 => 找出次數出現最多的數
def mode(v):
	counter = Counter(v)
	max_count = max(counter.values()) # 找到次數最多的次數為多少（可能不只一個）
	return [x_i for x_i,count in counter.items() if count == max_count]


# desperision 離散程度

# range => max-min
def data_range(v):
	return(max(v)-min(v))

# 變異數

def de_mean(v):
	v_bar = mean(v)
	return [v_i-v_bar for v_i in v ]

def variance(v):
	n = len(v)
	deviations = de_mean(v)
	return sum_of_squares(deviations)/n-1  # 平方差的平均 ps: 不是 /n , 是 /n-1

# 標準差

def standard_deviation(v):
	return math.sqrt(variance(v))

# 75% - 15%

def interquartitle_range(v):
	return quantile(v,0.75) - quantile(v,0.15)

# 共變異數 => 兩遍數分別距離平均值的程度 (較不準)

def covariance(x,y):
	n = len(x)
	return dot(de_mean(x),de_mean(y))/n-1

# 相關係數（correlation） 介在-1~1間 越接近1表越相關

def correlation(x,y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)

	if stdev_x > 0 and stdev_y > 0 :
		return covariance(x,y)/stdev_x/stdev_y
	else :
		return 0




num_friends = [100,20,100,30,70,10,100,100,70,100,60,60,70,70,70,90,60,22,33,66,77]
daily_minutes = [60,20,160,10,50,20,130,150,90,90,50,20,39,40,67,120,50,31,4,55,60]


friends_counts = Counter(num_friends)
print(friends_counts)

xs = range(101)
ys = [ friends_counts[x] for x in xs ]


num_points = len(num_friends)

largest_value  = max(num_friends)
smallest_value = min(num_friends)

sorted_value 	= sorted(num_friends)
smallest_value 	= sorted_value[0]
second_smallest = sorted_value[1]
second_largest  = sorted_value[-2]
midpoint = median(num_friends)

print("中位數:",midpoint)
print("百分位數(70%):",quantile(num_friends,0.7))
print("眾數:",mode(num_friends))
print("Range:",data_range(num_friends))
print("變異數:",variance(num_friends))
print("標準差:",standard_deviation(num_friends))
print("75% - 15%:",interquartitle_range(num_friends))
print("共變異數:",covariance(num_friends,daily_minutes))
print("相關係數:",correlation(num_friends,daily_minutes))


plt.scatter(num_friends,daily_minutes)
plt.axis('equal') # 讓x,y在同一個尺度
plt.show()

# plt.axis([0,101,0,10])
# plt.bar(xs,ys)
# plt.show()