# 統計document裡面各個元素有幾個

from collections import defaultdict # 當你檢查一個不存在的key時，他會補0

word_counts = defaultdict(int) # int()會補0

document = [ 'a','a','b','c','d','a','b']

for word in document:
	word_counts[word] += 1

print(word_counts)