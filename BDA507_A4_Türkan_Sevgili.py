# Q1.
# Please prepare a number array of 3 rows and 7 columns.
# The content should be the numbers from 9 to 100s with the incrementation value of 7.
# Then you should make a clone of this array with a different name.
# Then this copy array’s values should be changed to remainder of 8.
# For instance, the initial array held the values: 9, 16, 23, 30, ….
# After being copied to a new array the values should be adjusted as such: 1, 0, 7, 6 ….
#  (these are the remainder when the initial values are divided by 8).

import numpy as np
x =  np.arange(9,150,7).reshape(3,7)
print(x)

clone_x=x

print(clone_x)

for i in range(3):
    for j in range(7):
        print(x[i, j] % 8)


# Q2.
# Prepare a numpy array of 7 x 7 matrix with all its content having the value 9.
# Then please change the border content to 8 and the inside content to 7 separately.
# Please try to do it with the short cuts that we have done in the class (this is Part-A) as well as using 2 for loops (this is Part-B).

import numpy as np
#using no.full
all_9 = np.full((7, 7), 9, dtype=np.uint)
print(all_9)

print("8 on the border in the array")
all_9[0:7,0:7]=8
print(all_9)

print("7 inside in the array")
all_9[1:-1,1:-1] = 7
print(all_9)


# Q3.
# Please prepare the checkerboard pattern with using for loops as opposed to the one that we have done during our last class.
# The code for checkerboard pattern that we have done during class is as follows:


"""
print ("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x [1: : 2, : : 2] = 1
x [: : 2, 1 : : 2] = 1
print(x)
"""

all_0 = np.zeros((8,8),dtype=int)

for i in range(8):
    for j in range(8):
        if (i+j)%2==0 :
            all_0[i,j]=1
        else:
            all_0[i,j]=0
print(all_0)

# Q4.
# For Titanic dataset, please work on the “test.csv” file this time and do the following tasks (The file is also in the relevant folder for Week-4):
# (a) Get the dataset via pandas library,

import pandas as pd
titanic_test = pd.read_csv('test.csv')
print(titanic_test)

titanic_test.dtypes

# (b) display the dimensions (rows and columns),
titanic_test.shape# Check dimensions
# (418, 11)

# (c) show the first 10 lines,
print(titanic_test.head(10))  # Check the first 10 rows

# (d) show the descriptive statistics both for numeric and categorical data,
print(titanic_test.describe() )

categorical = titanic_test.dtypes[titanic_test.dtypes == "object"].index
print(categorical)
#  Index(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], dtype='object')

titanic_test[categorical].describe()

# (e) change the survived column to categorical data (as “yes” and “no” values),
#1.yol
titanic_test.survived=titanic_test.survived.astype(str)
print(titanic_test.survived)

#2.yol
index=np.where(titanic_train["Survived"]==1)
print(index)
titanic_train["Survived"].loc[index]="Y"
print(titanic_train.Survived)

index=np.where(titanic_train["Survived"]==0)
titanic_train["Survived"].loc[index]="N"


# (f) display the number of passengers that have used A-B-C-D-E-F cabins,
import numpy as np
char_cabin = titanic_test["Cabin"].astype(str) # Convert data to str
print(char_cabin)
new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter
print (new_Cabin)
new_Cabin = pd.Categorical(new_Cabin)
print (new_Cabin)
new_Cabin .describe()

# (g) display the number of passengers whose age is greater than 40 and male (then count the females that are greater 40 years of age),

index1 = np.where(titanic_test["Age"]>40)
print(index1)
greater_fourty=titanic_test.loc[index1]
print(greater_fourty)
greater_fourty.describe()
#77

index2=np.where(greater_fourty["Sex"]=="male")
print(index2)
sex_male=titanic_test.loc[index2]
print(sex_male)
sex_male.describe()
#47

index3=np.where(greater_fourty["Sex"]=="female")
print(index3)
sex_female=titanic_test.loc[index3]
print(sex_female)
sex_female.describe()
#30

# (h) count the number of missing values for Age column.
titanic_test["Age"].describe()
missing = np.where(titanic_test["Age"].isnull() == True)
len(missing[0])
#86


# Q5.
# Please plot the histograms for each of the columns in the dataset.
# You can decide on the details (such as figure sizes and bins) of the figures.
# The code that we have gone over in the class includes the relevant function you need to run.

titanic_test.dtypes

#PassengerId
titanic_test.hist(column='PassengerId',     # Column to plot
                   figsize=(9,6),           # Plot size
                   bins=20)                 # Number of histogram bins

#Pclass
titanic_test.hist(column='Pclass',  # Column to plot
                   figsize=(9,6),   # Plot size
                   bins=20)         # Number of histogram bins

#Age
titanic_test.hist(column='Age',     # Column to plot
                   figsize=(9,6),   # Plot size
                   bins=20)         # Number of histogram bins

#SibSp
titanic_test.hist(column='SibSp',   # Column to plot
                   figsize=(9,6),   # Plot size
                   bins=20)         # Number of histogram bins

#Parch
titanic_test.hist(column='Parch',   # Column to plot
                   figsize=(9,6),   # Plot size
                   bins=20)         # Number of histogram bins

#Fare
titanic_test.hist(column='Fare',    # Column to plot
                   figsize=(6,6),   # Plot size
                   bins=30)         # Number of histogram bins
