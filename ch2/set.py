s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
x = len(s)
print(x)

print(3 in s ) # 在set裡用in比較快
print(4 in s )

item_list = [1,2,3,4,1,2,3]
item_set = set(item_list)
print(item_set) # set裡只留下不ㄧ樣的元素



# all => 所有元素裡都true最後才true
# any => 其中任一元素為true就是true

print(all([True,1,{3}]))
print(all([True,1,{}]))
print(any([True,1,{}]))
