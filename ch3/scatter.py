from matplotlib import pyplot as plt 

friends = [80 ,100 ,1 , 60 ,12 ,78]
minutes = [175 , 180 , 120 , 100 , 200 , 230]
labels = ['a','b','c','d','e','f']

plt.scatter(friends,minutes)

for label,friend_count,minute_count in zip(labels,friends,minutes):
	plt.annotate(label,
				xy = (friend_count,minute_count), # 把label放到對的位置
				xytext = (5,-5), # label平移
				textcoords = 'offset points')


plt.show()