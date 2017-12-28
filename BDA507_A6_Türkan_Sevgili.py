'''
1. Please construct a two-dimensional numpy array composed of random integers (in a range of -10 to
38) with a size of 5 columns (cities A, B, C, D, and E) and 364 rows (days).
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(45)

number_days = 364
number_weeks = 52

#Create 364*5 multi dimensional array. Data in array is random.
temperatures = np.random.randint(-10,39,(364,5))
print(temperatures)

#Cities name
cities = [_ for _ in 'ABCDE']
temperatures=pd.DataFrame(temperatures,  columns=cities)

tempArray = np.array(temperatures)
#print(tempArray[:,0].mean())

#Dimensions of array
print("Dimensions of Array",tempArray.shape)

#temperatures.to_csv('df.csv', index=True, header=True, sep=' ')

'''
2. These are the measured temperatures and determine which of these 5 cities is the hottest one and
which of these is the coldest one simply by your code. You should not decide these manually, in other
words, your code should decide.
'''
list = []
for index,i in enumerate(cities):
    list.append(tempArray[:, index].mean())
    #print(tempArray[:, index].mean())

#Hottest city based on avg. temp.
minimumCity = cities[np.argmin(list)]
print("City '",minimumCity, "' is the hottest city")

#Coldest city based on avg. temp.
maximumCity = cities[np.argmax(list)]
print("City '",maximumCity, "' is the coldest city")

'''
3. Figure out which is the hottest day (with a comparison through 5 cities) again by your Python
code, please. Is it possible to look for a (statistically) significant difference? If so, how?
'''
# Mean temperature of each day
list2=[]
for index,day in enumerate(tempArray):
    list2.append(day.sum())
    #print(day.sum())

np.argmax(list2)
print(np.argmax(list2), ". day is the hottest day in all cities")


#bar graph
bar_width = 1
y=list2
N = len(y)
x = range(N)

plt.bar(x, y, bar_width, color="orange")
plt.show()

'''
4. Please find a way (among one of the python libraries) to visualize/demonstrate these 364 days with
a figure as an average of 5 cities. Hint: There should be 364 x 5 data points.
'''

# days array
days  = [k for k in range(number_days)]

list3=[]
for index,day in enumerate(tempArray):
    list3.append(day.mean())
    #print(day.sum())


import matplotlib.pyplot as plt

#scatter plot
plt.scatter(y=list3, x=days)
plt.xlabel('Days')
plt.ylabel('Mean Temperature')
plt.show()

#bar graph
bar_width = 1
y1=list3
N1 = len(y)
x1 = range(N)

plt.bar(x1, y1, bar_width, color="pink")
plt.show()

#line graph
plt.plot(x1, y1)
plt.show()


'''
5. Suppose that these 364 days are 52 weeks. Then please provide a weekly (average) illustration of
these cities and illustrate them via figures/plots. Hint: there should be 52 x 5 data points.
'''

# Weeks
weeks  = [k for k in range(number_weeks)]

# Calculation weekly mean of temperature of cities
weeklyAvgTemp = np.zeros(number_weeks)

for i in range(len(list3)):
    # return week numbers(mod 7)
    weeklyAvgTemp[i // 7] += list3[i]

# Calculate average by divided by 7 for each week
weeklyAvgTemp = weeklyAvgTemp/7

plt.scatter(y=weeklyAvgTemp, x=weeks)
plt.xlabel('Weeks')
plt.ylabel('Mean Temperature')
plt.show()