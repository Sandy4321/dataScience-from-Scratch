from matplotlib import pyplot as plt 


variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [ 256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [ x+y for x,y in zip(variance,bias_squared)]

xs = [ i for i,_ in enumerate(variance) ]
print(xs)


plt.plot(xs,variance, 'g-' , label = 'variance') # 'g-' => 綠色
plt.plot(xs,bias_squared, 'r-' , label = 'bias_squared') # 'r-' => 紅色
plt.plot(xs,total_error, 'b-' , label = 'total_error') # 'b-' => 藍色

plt.legend(loc=9) # 把label放在正中間
plt.xlabel('model complexity')
plt.ylabel('Bias-Variable')

plt.show()