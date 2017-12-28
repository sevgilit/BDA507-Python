
"""

BDA507 WEEK#7 FALL 2017-18

For taste:
https://selfdrivingcars.mit.edu/deeptrafficjs/

Outline:
- General Review (What have we done this term?)
- Programming Fundamentals:
    * Break
    * Continue
    * Recursion
- Some fancy stuff: Running PacMan
- Digits dataset
- China dataset

"""

"""

GENERAL REVIEW:
- Basic commands in Python
- Functions
- Libraries: Pandas, Numpy, Scipy, Matplot...
- Clustering & Classification

"""


"""
BREAK:
In the following example for loop breaks when the count value is 5. The print statement after the for loop displays
the sum of first 5 elements of the tuple numbers.
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1
    if count == 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)


"""
CONTINUE:
The continue statement is used in a while or for loop to take the control to the top of the loop without executing
the rest statements inside the loop. Here is a simple example.

In the above example, the for loop prints all the numbers from 0 to 6 except 3 and 6 as the continue statement returns
the control of the loop to the top

"""

for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)

"""
Errors and Exceptions:
Until now error messages haven’t been more than mentioned, but if you have tried out the examples you have probably
seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.
https://www.tutorialspoint.com/python3/python_exceptions.htm
"""

(x, y) = (5, 0)  # Zero division error
try:
    z = x / y
except ZeroDivisionError as e:
    z = e  # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
print(z)  # output: "integer division or modulo by zero"


"""
List of exceptions:
https://docs.python.org/3/tutorial/errors.html

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.

"""

#!/usr/bin/python3

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
temp_convert(100000)


"""
TASK: Please explain briefly what the code below does!
"""

#!/usr/bin/python3
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])


"""
ASSERTIONS:
An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program.
The easiest way to think of an assertion is to liken it to a raise-if statement
(or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false,
an exception is raised.
Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.
Programmers often place assertions at the start of a function to check for valid input,
and after a function call to check for valid output.
"""


#!/usr/bin/python
def KelvinToFahrenheit(Temperature):
   assert((Temperature >= 0),"Colder than absolute zero!")
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))


number = int(input('Enter a positive number:'))
# Enter a positive number:-1
assert (number > 0), 'Only positive numbers are allowed!'


"""
RECURSION:
- An expression, such as a polynomial, each term of which is determined by application of a formula to preceding terms.
- A formula that generates the successive terms of a recursion.

TASK-1: Use a loop-function (for or while loop) in order to give the following output regarding the user input. Let’s
assume that the user has entered 5 and your code should give the outputs from 5 to 1 and prints them on the screen.
5
4
3
2
1
Finito!
"""

# Countdown example that will produce the output as follows: n, n-1, n-2, ..... 3, 2, 1, 'Finito!'
def countdown(n):
    if n == 0:
        print("Finito!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

"""
TASK-2: Please modify the code above to get input from the user. And your script should provide the countdown from
this input until zero. You need to call the same function above.
"""


"""
Roughly speaking, recursion and iteration perform the same kinds of tasks:
Solve a complicated task one piece at a time, and combine the results.
 Emphasis of iteration:
- Keep repeating until a task is “done” e.g., loop counter reaches limit, linked list reaches null pointer.
 Emphasis of recursion:
- Solve a large problem by breaking it up into smaller and smaller pieces until you can solve it; combine the results.
e.g., recursive factorial function.

Which is better?
No clear answer, but there are known trade-offs.
“Mathematicians” often prefer recursive approach.
- Solutions often shorter, closer in spirit to abstract mathematical entity.
- Good recursive solutions may be more difficult to design and test.
“Programmers”, esp. w/o college CS training, often prefer iterative solutions.
- Somehow, it seems more appealing to many.
- Control stays local to loop, less “magical”. Compare iterative to recursive versions of factorial!
"""


"""
TASK-3: FIBONACCI
Here is Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
Thus, a term is the sum of previous two terms.
You are asked to find the nth term in Fibonacci series with iteration and recursion (two different functions).

def fibonacci_iter
...
...

def fibonacci_rec
...
...

"""


"""
DESIGNING RECURSIVE FUNCTIONS:
A recursive function just means a function that calls itself. But there must be some occasions when the function does not call itself, or else the program will run forever, like we saw above. A base case is the part of a recursive function where it doesn't call itself. In the example above, the base case was n<=0. Designing a recursive function requires that you carefully choose a base case and make sure that every sequence of function calls eventually reaches a base case.
In the next exercise, the base case has been programmed for you, but you will write the rest of the recursive function.
"""


"""
TASK-4A: FACTORIAL
You should provide two functions to calculate factorial, one with iteration and the other with recursion.

def factorial_iter:
...
...

def factorial_rec:
...
...

"""


"""Unscramble the lines to create a program that produces a recursive ruler-like design. For example, when n=3 the program should output the following design.
 
-
--
-
---
-
--
-

TASK-5: Please provide the necessary ordering to provide the output above:
...
def ruler(n):
else:
print('-')
if n == 1:
ruler(n - 1)
ruler(n - 1)
print(n * '-')
...
"""



"""
==================================
Color Quantization using K-Means
==================================
Performs a pixel-wise Vector Quantization (VQ) of an image of the summer palace (China), reducing the number of colors required to show the image from 96,615
unique colors to 64, while preserving the overall appearance quality.

In this example, pixels are represented in a 3D-space and K-means is used to find 64 color clusters. In the image processing literature, the codebook
obtained from K-means (the cluster centers) is called the color palette. Using a single byte, up to 256 colors can be addressed, whereas an RGB encoding
requires 3 bytes per pixel. The GIF file format, for example, uses such a palette.

For comparison, a quantized image using a random codebook (colors picked up randomly) is also shown.
"""

# Authors: Robert Layton <robertlayton@gmail.com>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#
# License: BSD 3 clause

print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time

n_colors = 64
# n_colors = 64


# Load the Summer Palace photo
china = load_sample_image("china.jpg")
print(china)
# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])
china = np.array(china, dtype=np.float64) / 255

print(china)
print(china.shape)

# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(china.shape)
print(w)
print(h)
print(d)
assert d == 3
image_array = np.reshape(china, (w * h, d))
print(image_array)
print("Fitting model on a small sub-sample of the data")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
print("done in %0.3fs." % (time() - t0))

# Get labels for all points
print("Predicting color indices on the full image (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print("done in %0.3fs." % (time() - t0))
print(labels)
n_digits = len(np.unique(labels))  # the number of labels are determined with the aid of unique formula
print(n_digits)

codebook_random = shuffle(image_array, random_state=0)[:n_colors + 1]
print("Predicting color indices on the full image (random)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random,
                                          image_array,
                                          axis=0)
print("done in %0.3fs." % (time() - t0))


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

# Display all results, alongside original image
plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (96,615 colors)')
plt.imshow(china)

plt.figure(2)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (64 colors, K-Means)')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure(3)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (64 colors, Random)')
plt.imshow(recreate_image(codebook_random, labels_random, w, h))
plt.show()


"""
========================================================================================================================
======================= Classification applications on the handwritten digits data =====================================
========================================================================================================================
In this example, you will see two different applications of Naive Bayesian Algorithm on the
digits dataset.
"""

print(__doc__)

import pylab as pl
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from time import time
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

########################################################################################################################
##################################### GETTING THE DATA & PREPARATIONS ##################################################
########################################################################################################################

np.random.seed(42)
digits = load_digits()  # the whole dataset with the labels and other information are extracted
data = scale(digits.data)  # the data is scaled with the use of z-score
n_samples, n_features = data.shape  # the no. of samples and no. of features are determined with the help of shape
n_digits = len(np.unique(digits.target))  # the number of labels are determined with the aid of unique formula
labels = digits.target  # get the ground-truth labels into the labels

print(labels)
print(digits.keys())  # this command will provide you the key elements in this dataset
print(digits.DESCR)  # to get the descriptive information about this dataset

pl.gray()
pl.matshow(digits.images[8])
pl.show()
print(digits.images[0])

########################################################################################################################
########################################################################################################################

from sklearn.model_selection import train_test_split  # some documents still include the cross-validation option but it no more exists in version 18.0
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pylab as plt
y = digits.target
X = digits.data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

########################################################################################################################
########################################################################################################################

gnb = GaussianNB()
fit2 = gnb.fit(X_train, y_train)
predicted = fit2.predict(X_test)
print(confusion_matrix(y_test, predicted))
print(accuracy_score(y_test, predicted)) # the use of another function for calculating the accuracy (correct_predictions / all_predictions)
print(accuracy_score(y_test, predicted, normalize=False))  # the number of correct predictions
print(len(predicted)) # number of all of the predictions


import pickle
filename = 'finalized_model.csv'
pickle.dump(fit2, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

########################################################################################################################
########################################################################################################################

gnb = GaussianNB()
fit2 = gnb.fit(X, y)
predictedx = fit2.predict(X)
print(confusion_matrix(y, predictedx))
print(accuracy_score(y, predictedx)) # the use of another function for calculating the accuracy (correct_predictions / all_predictions)
print(accuracy_score(y, predictedx, normalize=False))  # the number of correct predictions
print(len(predictedx))  # number of all of the predictions

unique_y, counts_y = np.unique(y, return_counts=True)
print(unique_y, counts_y)
unique_p, counts_p = np.unique(predictedx, return_counts=True)
print(unique_p, counts_p)
print((predictedx == 0).sum())
########################################################################################################################
########################################################################################################################
