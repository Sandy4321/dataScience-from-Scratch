# zip 

list1 = ['a','b','c']
list2 = [ 1, 2, 3]

list_zip = zip(list1,list2)


# unzip set

pairs = [('a',1),('b',2),('c',3)]
print(pairs)

letters,numbers = zip(*pairs)
print(letters,numbers)


def add(a,b) : return a+b

# unzip list

print(add(*[1,2]))