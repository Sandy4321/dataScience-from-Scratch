even_number = [ x for x in range(5) if x%2 == 0] # 同時計算list裡的所有元素
print(even_number)

zeros = [ 0 for _ in even_number] # 造一個與even_number一樣大的list但是元素都是0
print(zeros)

# 雙層迴圈，先跑x迴圈再跑y迴圈，並把結果都放進(x,y)

pairs = [(x,y) 
		for x in range(10)
		for y in range(10)]

print(pairs) # 100對set

increasing_pairs = [(x,y)
				   for x in range(10)
				   for y in range(x+1,10)] 
