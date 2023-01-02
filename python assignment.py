#!/usr/bin/env python
# coding: utf-8

# # write a python program to calculate the length of a string

# In[9]:


str = input( "Enter a string:")
counter=0
for s in str:
    counter= counter+1
print( "Length of the string is:", counter)


# # write a python program to calcute the square root.

# In[11]:


number=float(input("Enter the number:"))
sqrt= number** 0.5
print("square root of the given number is:", sqrt)


# # write a python program to convert temperature in celsius to temperature in farenheit

# In[18]:


celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print('%.2f celcius is: %0.2f fahrenheit' %(celsius, fahrenheit))


# # write a python program for a data type needed for given data .( 10,4.5,2+6j)

# In[19]:


num1= 10
print(num1, 'is of type', type(num1))
num2= 4.5
print(num2, 'is of type', type(num2))
num3= 2+6j
print(num3,' is of type', type(num3))


# In[ ]:




