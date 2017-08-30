class Set : 

	def __init__(self,values=None):
		# 建構式 => 初始化
		self.dict = {}
		if values is not None :
			for value in values:
				self.add(value)
	def __repr__(self):
		# 敘述此函式在做什麼
		return "Set : " + str(self.dict.keys())

	def add(self,value):
		self.dict[value] = True

	def contains(self,value):
		return value in self.dict

	def remove(self,value):
		del self.dict[value]

s = Set([1,2,3])

print(s)
s.remove(3)
print(s.contains(3))


