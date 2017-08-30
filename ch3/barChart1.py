from collections import Counter
from matplotlib import pyplot as plt 


grades = [80,90,90,80,70,0,80,80,100,60,70,70,0]
decile = lambda grade : grade

histogram = Counter(decile(grade) for grade in grades) # Counter計算個元素的數量

print(histogram)

plt.bar([ x-4 for x in histogram.keys()],histogram.values(),8)

plt.axis([-5,105,0,5])
plt.xlabel('Decile')
plt.ylabel('# of students')
plt.title('Distribution of exam 1 Grades')
plt.xticks([10 * i for i in range(11)])
plt.show()