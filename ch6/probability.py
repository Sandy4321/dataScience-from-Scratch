from collections import Counter
import math, random

def random_kid():
	return random.choice(['boy','girl'])

both_girls  = 0
older_girl  = 0
either_girl = 0

random.seed(60)

for _ in range(10000):
	youger = random_kid()
	older  = random_kid()
	if older == "girl":
		older_girl  += 1to
	if older == "girl" and youger == "girl":
		both_girls  += 1
	if older == "girl" or  youger == "girl":
		either_girl += 1 


print("P(both | older ) : ", both_girls/older_girl)
print("P(both | either ) : ", both_girls/either_girl)
