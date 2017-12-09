
'''
Q1. Please provide a class in Python 3 that will include 3 different functions for rectangular prisms.
The first function will calculate the surface area of a rectangular prism,
the second one will calculate the volume of this prism,
and the third one should properly print these two calculated values on the console.
'''

#Formulas
#Area = 2(ab+bc+ac)
#Volume = a.b.c

class Prism():
    def __init__(self, a,b,c):
        self.side1 = a
        self.side2 = b
        self.side3 = c
    def Area(self):
        return 2*((self.side1*self.side2)+(self.side2*self.side3)+(self.side1*self.side3))

    def Volume(self):
        return (self.side1*self.side2*self.side3)

NewPrism = Prism(2,1,1)
print(NewPrism.Area())
print(NewPrism.Volume())

'''
Q2. You are expected to understand the following class and provide the necessary comments to the given places
(annotated with “# ….”).
'''

class ComplexNumber:
    def __init__(self,r = 0,i = 0): # sets "init'ial" state to objects/instances, use self argument. Returns a ComplexNumber object with the given r and i.
        self.real = r # self usage => instance variable (per object)
        self.imag = i # self usage => instance variable (per object)
    def getData(self): # define getData() function
        print("{0}+{1}j".format(self.real,self.imag)) # ………………………………………….
c1 = ComplexNumber(2,3) # Create a new ComplexNumber object. c1 now contains an object of class ComplexNumber. c1.value is now r=2 and i=3
# Output 2+3j
c1.getData() # Call getData() function
c2 = ComplexNumber(5) # Create another ComplexNumber object. c2 now contains an object of class ComplexNumber. c1.value is now 5
# Output (5,0,10)
c2.attr = 10 # Create a new attribute 'attr'


'''
Q3. Please make use of the following Customer class with providing Sarah and Hakeem two different accounts and a series of deposits.
Please try to cover all the functions and attributes.

class Customer(object):
"""A customer of ABC Bank with a checking account. Customers have the following properties:
Attributes:
name: A string representing the customer's name.
balance: A float tracking the current balance of the customer's account.
"""
def __init__(self, name, balance=0.0):
"""Return a Customer object whose name is *name* and starting
balance is *balance*."""
self.name = name
self.balance = balance

def withdraw(self, amount):
"""Return the balance remaining after withdrawing *amount* dollars."""
if amount > self.balance:
raise RuntimeError('Amount greater than available balance.')
self.balance -= amount
return self.balance

def deposit(self, amount):
"""Return the balance remaining after depositing *amount* dollars."""
self.balance += amount
return self.balance
'''


class Customer(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

Sarah = Customer('Sarah',500)
Hakeem = Customer('Hakeem',1000)

print(Sarah.withdraw(100))
print(Sarah.deposit(500))

print(Hakeem.withdraw(250))
print(Hakeem.deposit(400))

'''
Q4. You are expected to provide the descriptive statistics for the Boston dataset.
'''
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

bos=pd.DataFrame(boston.data)
print(bos.head())

bos.columns=boston.feature_names
print(bos.head())

print(boston.target.shape)

bos['PRICE']=boston.target
print(bos.head())

print(bos.describe())

'''
Q5. You are expected to provide a series of plots that you find logical for describing the Boston dataset as we did in the class for the Iris dataset.
You do not have to provide all the different kind of figures but try to be precise while trying to illustrate the dataset.
You can make use of the following link for the seaborn library: http://seaborn.pydata.org/examples/
'''
import matplotlib.pyplot as plt
attr=bos['PRICE']
plt.hist(attr)
plt.hist(attr,bins=50)

# univariate plots to see individual distribution
sns.distplot(a=bos['PRICE'],rug=True) #kde=true & hist=true by default
sns.distplot(a=bos['AGE'],rug=True)

# factorplot
sns.factorplot(x="PRICE",y="AGE",data=bos,hue="LSTAT")

# let you easily view both a joint distribution and its marginals at once.
# A seaborn jointplot shows bivariate scatterplots and univariate histograms in the same figure
# Can't provide hue in joint plot
sns.jointplot(x="PRICE", y="AGE", data=bos,size=5,kind="scatter") #scatter is default kind
sns.jointplot(bos['PRICE'],bos['LSTAT'],kind='hex')
sns.jointplot(bos['PRICE'],bos['LSTAT'],kind='kde')
# sns.plt.show()

# A clear picture of distribution can be seen with pairplot. Pairplot displays distribution of data
# according to every combination.
# In pair plot, members except diagonals are joint plot
print(bos.columns)
sns.pairplot(bos,hue="PRICE",diag_kind="kde")
# sns.plt.show())
