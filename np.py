#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# In[4]:


a1 = np.arange(10)  # Create a range from 0 to 9 i.e 10 Values
print(a1)  # Will print out all the values from 0 to 9 i.e [0 1 2 3 4 5 6 7 8 9]
print(a1.shape)  # The shape represents the total number of values that will be displayed

# In[5]:


a2 = np.arange(0, 10, 2)
print(a2)  # [0 2 4 6 8]
print(a2.shape)  # The shape represents the total number of values that will be displayed. In this case (5, )

# In[6]:


a3 = np.zeros(5)  # Prints an array of zeros i.e [0. 0. 0. 0. 0.]
print(a3)
print(a3.shape)

# In[7]:


a4 = np.zeros((2, 3))  # 2D Array - 2Rows 3 Colums with all the values being zeros
print(a4)

# In[8]:


# Print out an ND array with specific a value
a5 = np.full((2, 3), 5)  # 2D Array - 2Rows 3 Columns with all the values being 5
print(a5)

# In[9]:


# Create an Identity Matrix
a6 = np.eye(4)  # A 4X4 Identity Matrix using a 2D Array
print(a6)

# In[29]:


# Create an Array Filled with Random Numbers
a7 = np.random.random((2, 4))  # 2D array with 4 columns containing random values
print(a7)

# In[30]:


myList = [1, 3, 6, 9, 12]
r1 = np.array(myList)

# Printing the Indeces of an Array
print(r1[1])
print(r1[2])

myList2 = [2, 4, 6, 8, 10]
r2 = np.array([myList, myList2])
print(r2)
print(r2.shape)  # The dimensions of the array i.e (2, 5)
print(r2[1, 4])

# In[12]:


# Boolean Indexing

print(r1 > 5)  # Returns True/False for all values i.e if they are greater(True) or less(False) than 5
# [False False  True  True  True]


# In[13]:


print(r1[r1 > 5])  # Same as the prev example but now returns all the values that are True
# [ 6  9 12]


# In[14]:


# How to print all odd Numbers in a sequence
nums = np.arange(100)
odd_nums = nums[nums % 2 == 1]
print(odd_nums)

# In[53]:


# Slicing Arrays
a = np.array([[1, 2, 3, 4, 5],
              [4, 5, 6, 7, 8],
              [9, 8, 7, 6, 5]])

b1 = a[1:3]  # Row 1 to Row 3, Row 3 is however not included so Row 1 and Row 2 will only be returned
b2 = a[1:3, :3]  # Returns Row 1 and Row 2 and Only the First 3 Columns(i.e the frst 3 values of each list) of each Row
b3 = a[0:, 2:]

print(b1)
print(b2)
print(b3)
print(b2.shape)

# In[57]:


# Math on Arrays
x1 = np.array([[9, 53, 4, 46], [5, 7, 8, 12]])
y1 = np.array([[5, 8, 44, 32], [78, 19, 8, 5]])

# Sum
print("Sum = ", x1 + y1)
print(np.add(x1, y1))
# Subtract
print("Subtract = ", x1 - y1)
print(np.subtract(x1, y1))
# Multiply
print("Multiply = ", x1 * y1)
print(np.multiply(x1, y1))
# Divide
print("Divide = ", x1 / y1)
print(np.divide(x1, y1))

# In[67]:


names = np.array(['Rikk', 'Nancy', 'Evans'])
height = np.array([1.8, 1.4, 1.9])
weight = np.array([54, 65, 63])

bmi = weight / height ** 2  # Calculate the BMI(Body Mass Index) and stores the result as an NumpyArray
print(bmi)  # We get the BMI of everyone
print("Overweight:", names[bmi > 25])  # Returns the name of the person who is overwight i.e BMI exeeds 25
print("Underwight:", names[bmi < 18.5])  # Returns the name of the person who is Underwight i.e BMI below 18
print("Healthy:",
      names[(bmi >= 18.5) & (bmi <= 25)])  # Returns the name of the person who is neither overwight nor underwight

# In[71]:


# Dot Product
x2 = np.array([2, 4, 6])
y2 = np.array([1, 3, 5])

print(np.dot(x2, y2))  # 2x1 + 4x3 + 6x5 = 44 i.e the Dot Product of the matrices

x3 = np.array([[1, 2, 3], [4, 5, 6]])
y3 = np.array([[7, 8], [9, 10], [11, 12]])

print(np.dot(x3, y3))  # Matrix Multiplication

# In[ ]:
