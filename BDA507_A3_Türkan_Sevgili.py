#TASK-1
# Please write a function to find the minimum number among three given integers. Your function should be different than the example given in the class. Here is a hint:
#def maxOfThreeNum (num1, num2, num3):
#Then you should call the function with different integer sets in order to check whether it works properly.

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
num3 = int(input("Number3: "))

def get_minOfThreeNum (a,b,c):
    #using min function
    return(min(a,b,c))
print(get_minOfThreeNum (num1, num2, num3))


#TASK-2
# Please get 6 input numbers (as float or as double) from the user as the coordinates of the three points.
# These points correspond to a triangle. Please calculate the length of each side of this triangle(you can use the distance formula for the points).
# You should provide a distance formula for this calculation.
# Then you should provide an area function and calculate the area of this triangle. (Hint: You can use the U-formula for this).
# You should then decide whether this is an obtuse, right or acute triangle (as in the previous assignment).

input1 = float(input("Input1: "))
input2 = float(input("Input2: "))
input3 = float(input("Input3: "))
input4 = float(input("Input4: "))
input5 = float(input("Input5: "))
input6 = float(input("Input6: "))

def calculateArea(side1,side2,side3):
    #First calculate the area of this triangle with using U-formula.
    s = (side1 + side2 + side3) / 2
    A = (s * (s - side1) * (s - side2) * (s - side3)) ** (0.5)
    print("Area: " + str(A))

#Then define the 3 sides of triange and check the triangle is an obtuse, right or acute triangle.
def triangle(x1, x2, y1, y2, z1, z2):
    AB = (((((x2 - x1) ** 2.0) + ((y2 - y1) ** 2.0)) ** (0.5)))
    AC = (((((x2 - x1) ** 2.0) + ((z2 - z1) ** 2.0)) ** (0.5)))
    BC = (((((y2 - y1) ** 2.0) + ((z2 - z1) ** 2.0)) ** (0.5)))
    # Check sides of a triangle are eligible to provide a triangle
    if AB < AC + BC and AC < AB + BC and BC < AB + AC:
        # Check triangle is a right, acute, or obtuse
        if AB ** 2 == (AC ** 2) + (BC ** 2) or AC ** 2 == (AB ** 2) + (BC ** 2) or BC ** 2 == (AB ** 2) + (AC ** 2):
            print('This is an right triangle')
            calculateArea(AB,AC,BC)
        elif AB ** 2 < (AC ** 2) + (BC ** 2) or AC ** 2 < (AB ** 2) + (BC ** 2) or BC ** 2 < (AB ** 2) + (AC ** 2):
            print('This is an acute triangle')
            calculateArea(AB,AC,BC)
        elif AB ** 2 > (AC ** 2) + (BC ** 2) or AC ** 2 > (AB ** 2) + (BC ** 2) or BC ** 2 > (AB ** 2) + (AC ** 2):
            print('This is an obtuse triangle')
            calculateArea(AB,AC,BC)
    else:
        print('This is not a triangle')

triangle(input1, input2, input3, input4, input5, input6)


#TASK-3
# You have such a list of strings:
# color = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
# Your function or script should put this list in alphabetical order than write this ordered list into a new text file. Then it should open the list and print them on the console.

#First sort the list.
color = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
color.sort(key=None, reverse=False)
print(color)

with open('color_ordered_list.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)
content = open('color_ordered_list.txt')
print(content.read())


#TASK-4
# Your code should look for the amino acid patterns like (ACCCA or ACCA or ABA) and (AAABB or BBBBBAAACCC) in a huge random string of A, B, and C’s.
# You can set up your own amino acid sequence for testing. You are suggested to use the library for regular expressions. Here is a sample sequence to test:
# AAACACCCCBAAAAACBBBBABBCCCABAAABBAAAAAAAAAABBBBBAAABCCCACCCCBBBBBAAA
# It is sufficient to have a return value as true or false for the time being.

import re

def research(amino_acid_pattern):
    if re.search('[AC{3}A]', amino_acid_pattern) or re.search('[ACCA]', amino_acid_pattern) or re.search('[ABA]', amino_acid_pattern):
        if re.search('[ACCCA]', amino_acid_pattern) or re.search('[B{5}A{3}C{3}]', amino_acid_pattern):
            return ('TRUE!')
        else:
            return ('FALSE!')

print(research("AAACACCCCBAAAAACBBBBABBCCCABAAABBAAAAAAAAAABBBBBAAABCCCACCCCBBBBBAAA"))


#TASK-5

# You should make the file named “BMI_data.txt” read in python 3.
# Then you are required to calculate the BMI values for each of the participant as a new column at the rightmost
# part as “ID Name Surname Gender Height Weight BMI”. BMI (also known as body mass index) is a common biological index calculated by the mass over height ratio.
# For more information: https://en.wikipedia.org/wiki/Body_mass_index
# For providing an answer to this question, you need to calculate it via the given formula:
# BMI = weight (kg) / [height (m)]2
# Present the participants with the highest and lowest values in height, weight, and BMI.
# (Hint: You can use any built-in function in python for maximum values). Finally provide a figure that include these people (x-axis as height*height and y-axis as weight).

# Open and read the text with a matrix
matrix = []
with open('BMI_data.txt') as f:  # a with block will auto close your file after the statements within it
    for line in f:
        line = line.strip()  # strip off any trailing whitespace(including '\n')
        matrix.append(line.split())


# print(matrix)

# Find the text file row number.
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


file_length = file_lengthy('BMI_data.txt')
print(file_length)
xaxis = []
yaxis = []

# Append the BMIs for each row of the matrix.
for x in range(0, (file_length)):
    if x == 0:
        matrix[0].append('BMI')
    else:
        height = float(matrix[x][4])
        weight = float(matrix[x][5])
        print(height)
        print(height**2)
        xaxis.append(height**2)
        yaxis.append(weight)
        BMI = weight / (height ** height)
        BMI = str(BMI)
        matrix[x].append(BMI)

print(matrix)

# Create a new text file that not a matrix.
with open('BMI_data2.txt', "w") as myfile:
    for line in matrix:
        print(line)
        for row in line:
            print(row)
            myfile.write("%s\t" % row)
        myfile.write("\n")
open('BMI_data2.txt')

# Let's visualize the BMI data. (x-axis as height*height and y-axis as weight).

import matplotlib.pyplot as plt

print(xaxis)
print(yaxis)

plt.plot(xaxis, yaxis)
# Set the x axis label of the current axis.
plt.xlabel('height^2')
# Set the y axis label of the current axis.
plt.ylabel('weight')
# Set a title
plt.title('BMI graph!')
# Display a figure.
plt.show()
