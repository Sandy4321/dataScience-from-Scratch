from matplotlib import pyplot as plt
from collections import Counter
import math, random

# 連續分佈

def uniform_pdf(x):
	return 1 if x > 0 and x < 1 else 0

def unifrom_cdf(x):
	if   x < 0 : return 0
	elif x < 1 : return x
	else : return 1

# 常態分佈

def normal_pdf(x, mu=0, sigma=1):
	sqrt_two_pi = math.sqrt(2*math.pi)
	return (math.exp(-(x-mu)**2/2/(sigma)**2)/(sqrt_two_pi*sigma))

def normal_cdf(x ,mu=0, sigma=1):
	return (1 + math.erf((x-mu)/math.sqrt(2)/sigma))/2

xs = [ x/10 for x in range(-50,50)]

# mu = 0 , sigma =1 => 標準常態分佈

# plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
# plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
# plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
# plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-',label='mu=-1,sigma=1')
# plt.legend() # 顯示Label 可用 loc = number 來設定位置
# plt.title('Various Normal pdf')
# plt.show()


# plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
# plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
# plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
# plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-',label='mu=-1,sigma=1')
# plt.legend() # 顯示Label 可用 loc = number 來設定位置
# plt.title('Various Normal cdf')
# plt.show()


# 中央極限定理

def bernouli_trial(p):
	return 1 if random.random() < p else 0

def binomail(n,p):
	return sum(bernouli_trial(p) for _ in range(n))

def make_hist(p,n, num_points):
	data = [binomail(n,p) for _ in range(num_points)]
	histogram = Counter(data)
	plt.bar([x for x in histogram.keys()],
			[y/num_points for y in histogram.values()],
			0.8,
			color= '0.75')
	mu = n * p 
	sigma = math.sqrt( n * p * (1-p))

	xs = range(min(data),max(data)+1)
	ys = [normal_cdf(i + 0.5 ,mu,sigma)-normal_cdf(i-0.5,mu,sigma) for i in xs ]

	plt.plot(xs,ys)
	plt.title('Binomial Distribution vs. Normal Approximation')
	plt.show()

make_hist(0.75,100,100000)



