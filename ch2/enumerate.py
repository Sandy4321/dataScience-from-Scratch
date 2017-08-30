
# enumerate => 產生(索引,元素)的組合

documents = [1,2,3,4,5]

for i,doc in enumerate(documents):
	print(i,doc)

print('=====================')

# 只需要索引的話以python的模式

for i,_ in enumerate(documents):
	print(i)


