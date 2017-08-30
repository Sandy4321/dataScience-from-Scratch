from matplotlib import pyplot as plt 

test_grade1 = [99,90,85,97,80]
test_grade2 = [100,85,60,90,70]

plt.scatter(test_grade1,test_grade2)
plt.axis('equal') # 讓x,y在同一個尺度
plt.show()