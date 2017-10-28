# Task1: Please write a function in python 3 to calculate the absolute value of a given number (without using the abs() function of course).
# The absolute value is important for distance, as you might probably remember. You should provide a proper name for the function and one argument.
# It should print the absolute value of the given integer on the console.

def absolute(x):
     if (x < 0):
     #if x is smaller than 0, we can multiply by -1 to be positive.
        print(x*(-1))
     else:
        print(x)

absolute(-525)

# Task2: Please write a function in python 3 to check whether given 3 numbers as the sides of a triangle are eligible to provide a triangle.
# We all know that the side lengths such as 3, 11, 15 cannot make a triangle, since 15 is greater than the sum of other numbers.
# In addition to this, you are also check if this triangle is a right, acute, or obtuse triangle.

# Any side of a triangle must be smaller than the sum of the other two sides.
# x<y+z
# y<x+z
# z<x+y

# Acute Triangle	An acute triangle has three angles that each measure less than 90 degrees.
# Obtuse Triangle	An obtuse triangle is a triangle with one angle that is greater than 90 degrees.
# Right Triangle	A right triangle is a triangle with one 90 degree angle.

def triangle(x,y,z):
    #Check sides of a triangle are eligible to provide a triangle
    if x<y+z and y<x+z and z<x+y:
        #Check triangle is a right, acute, or obtuse
        if x^2==(y^2)+(z^2) or y^2==(x^2)+(z^2) or z^2==(x^2)+(y^2):
            print('This is an right triangle')
        elif x^2<(y^2)+(z^2) or y^2<(x^2)+(z^2) or z^2<(x^2)+(y^2):
            print('This is an acute triangle')
        elif x ^ 2>(y ^ 2)+(z ^ 2) or y ^ 2>(x ^ 2)+(z ^ 2) or z ^ 2>(x ^ 2)+(y ^ 2):
            print('This is an obtuse triangle')
    else:
        print('This is not a triangle')

triangle(3,11,15)



# Task3: There are three Boolean objects. As you should remember, Boolean objects hold True or False values. You would like to calculate how many of these three objects hold True values.
# You are advised to use if-elif-else conditions for these calculations. You do not have to provide a function for this but you are recommended to do so.
# Let’s assume that x, y, z = True, False, False. Your function should give the output 1 for the number of True objects and will write x as the True objects and others as False.

def boolean_objects (x,y,z):
    boolean_list=[x,y,z]
    count_True = 0
    count_False = 0
    for object in boolean_list:
     if object:
         #if object is True increase the count_True
         count_True += 1
     else:
         #if object is True increase the count_True
         count_False+=1
    if count_True==0:
        print('All x,y,z are False')
    else:
        #print True and False objects numbers
        print('Number of True objects:',count_True, '\nNumber of False objects:',count_False)

boolean_objects (True, False, False)


# Task4: You are given a list of names as in the A1. We can directly bring it as follows:
# nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]
# You are asked to check if there is “Asli” in this list and please calculate how many of these. (If the name is in the list please print it as “yes in the list” else “not in the list”).
# Then check for “Kemalettin” in this list and please indicate how many of them there are in the list.
# To calculate the total number of names. Hint: There are 15 names in this list but how to calculate it with a for/while loop.
# To calculate the number of names that contain the letter a (uppercase a or lowercase a do not matter).


nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]

#Function of any name is in the nameList
def find_name (x):
    count=0
    for name in nameList:
        if name==x:
            count +=1
    if count>0:
        print('Yes,', x,'in the list')
    else:
        print('No,' , x,' not in the list')

find_name ("Asli")
find_name ("Kemalettin")


#Total number of names in nameList
nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]
count = 0
for name in nameList:
    count += 1
print("Total number of students:",count) #Total number of students: 15


#Number of names that contain the letter a (uppercase a or lowercase a do not matter)
nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]
contain_A_list=[]
for name in nameList:
    for char in name:
        if char=="A" or char=="a":
            contain_A_list.append(name)
            #if we do not take break, names which contains letter a more than one add multiple times.
            break
print('Number of names that contain the letter a:', len(contain_A_list))
print(','.join(contain_A_list))


# Task5: You are asked to calculate the list and sum of numbers divisible by 13 and that are odd (evens are excluded) from 100 to 999 by using a for/while loop.
# For instance: 105 is both divisible by 13 and is an odd number but not 118 (which is divisible by 13 but an even number).
# You may create an empty list object, append each tested item and sum the content at the very final step.,

list = []
count=0
sum=0
for x in range(100, 999):
    if (x % 13 == 0) and (x % 2 == 1):
        list.append(str(x))
        count+=1
        #sum of each tested item which divisible by 13 and is an odd
        sum=sum+x
print(count,'numbers are divisible by 13 and they are odd.' ,'Numbers are:',','.join(list), 'Sum of these numbers are', sum)


# Extra: Please check if a given number is a perfect number by using for/while loops in python 3.
# A perfect number is a number that the positive divisors of that number sums up to that number.
# For instance, 28 is equal to 1 + 2 + 4 + 7 + 14 all of which are the positive divisors of 28.


def get_perfect_numbers(max_number):
    sum=0
    perfect_number=[]

    for x in range(1,max_number):
        for y in range(1,x):
            if x % y==0:
                sum=sum+y
        #print(x, "-", sum)
        if sum==x:
             perfect_number.append(x)
        sum=0
    print('Perfect numbers:',perfect_number)
get_perfect_numbers(10830)