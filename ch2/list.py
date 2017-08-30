# List

x = range(10)

first_three = x[:3]
print(first_three)
three_to_end = x[3:]
print(three_to_end)
one_to_four = x[1:5]
print(one_to_four)
last_three = x[-3:]
print(last_three)
without_first_last = x[1:-1]
print(without_first_last)

print(  1 in [0,1,2,3] )
print(  4 in [0,1,2,3] )

x = [1,2,3]
x.extend([4,5,6]) #在List最後面加入多個元素
print(x)
x.append(7) # 在List最後面加入元素
print(x)
print(x[-1])

a,b = [1,2] # 分別將 a => 1 , b => 2
print(a,b)
 
_,y = [1,2] # 不在意第一個元素指派給誰
print(y)





