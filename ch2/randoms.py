import random

# random() => 亂數產生0-1的小小數
four_uniform_randoms = [random.random() for _ in range(4)] 
print(four_uniform_randoms)

random.seed(10) # 用來產生亂數的種子,只要seed值一樣，產生的亂數就會一樣
print(random.random())
random.seed(10)
print(random.random())
random.seed(5)
print(random.random())

random.seed() # 不設定seed

print(random.randrange(10))  # 從range(10) => 0-9隨機挑一個數字
print(random.randrange(3,6)) # 從3,4,5隨機挑一個數字


up_to_ten = [i for i in range(10)]
random.shuffle(up_to_ten) # shuffle隨機打亂List的順序
print(up_to_ten)

# choice => 從List元素裡隨機挑一個
my_best_friends = random.choice(['Alice','Bob','Charlie']) 
print(my_best_friends)

lottery_numbers = range(60)

# sample(List名稱,要挑幾個數字) => 不會重複挑選到已挑選過的數字
winning_numbers = random.sample(lottery_numbers,6)
print(winning_numbers)

# 允許重複挑選
random.seed(10)
numbers = [random.choice(range(60)) for _ in range(10)]
print(numbers)





