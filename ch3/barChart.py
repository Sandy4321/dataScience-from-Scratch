from matplotlib import pyplot as plt 


movies = ['Annie Hall','Ben-Hur','Casablanca']
num_oscars = [5,11,3]

xs = [i  for i,_ in enumerate(movies)]

plt.bar(xs,num_oscars)
plt.ylabel('# of Academy Awards')
plt.xlabel('My favorite Movies')
plt.show()