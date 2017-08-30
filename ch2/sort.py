x = [-4,1,2,3,5]
y = sorted(x) # 排序完不蓋掉x
print(y)
print(x)
x.sort() # 排序完蓋掉x 
print(x)

y = sorted(x,key=abs,reverse = True) # key根據後面函示計算的結果來排序, reverse = True 由大到小排序
print(y)


