#!/usr/bin/env python
# coding: utf-8

# In[8]:


#to calculate the area of circle with radius 7

radius = float(input("please enter the radius of the given circle:" ))
area_of_the_circle = 3.14 * radius*radius
print("the area of the given circle is:",area_of_the_circle)
print("the area of the circle with radius {} is area {}".format(radius,area_of_the_circle))


# In[23]:


#to calculate perimeter of the circle with radius 10.2
radius = float(input("please enter the radius of the given circle:" ))
perimeter_of_the_circle = 2 * 3.14 * radius
print("the perimeter of the given cricle is:",perimeter_of_the_circle)
print("the perimeter of the circle with radius {} is perimeter {}" .format(radius,perimeter_of_the_circle))


# In[16]:


#to calculate area of circle with radius (float) (collect using input function)
radius = float(input("please enter the radius of the given circle:" ))
area_of_the_circle = 3.14 * radius*radius
print("the area of the given circle is:",area_of_the_circle)
print("the area of the circle with radius {} is area {}".format(radius,area_of_the_circle))


# In[36]:


#collect radius and height from user (float)
radius = float(input("enter the radius:" ))
height = float(input("enter the height:" ))
volume = 3.14 * radius * 2 *height
print("the volume of the cylinder is:", volume)


# In[38]:


#calculate the area of cone
radius = float(input("enter the radius of cone:" ))
height = float(input("enter the height of cone:" ))
area = 3.141 * radius * (radius + math.sqrt(radius*radius + height*height))
print("surface area =",area)
print(type(radius))


# In[11]:


num1 = input("the first num: ")
num2 = input("the second num: ")
sum = float(num1) + float(num2)
print("the sum of num1 {} and num2 {} is {}".format(num1,num2,sum))


# In[9]:


#simple interset
p =int(input("enter the principal amount is:" ))
t =int(input("enter the time period is:" ))
r = int(input("enter the rate is:" ))
si =(p * t * r) / 100
print("the simple_interset is",si)
print(type(si))
print("the simple_interset with p {} and t {} and r {} is {}" .format(p,t,r,si))


# In[5]:


#compond interset
p =int(input("enter the principal is:"))
t =int(input("enter the time period is:" ))
r = int(input("enter the rate is:" ))
amount = principal * (pow((1 + rate / 100),t))
ci =amount - principal
print("the principal is:",p)
print("the time period is:",t)
print("the rate is:",r)
print("the compond_interset is",ci)




# In[14]:


#area of circle
def findarea(r):
    pi = 3.141
    return pi * (r*r)
print("area of circle is:",findarea(3))


# In[18]:


#sum of squres of natural number
def squresum(n):
    sm = 0
    for i in range(1,n+1):
        sm = sm + (i * i)
    return sm
n = 4
print(squresum(n))


# In[20]:


#cube of sum of natural number
n = 5
s = 0
for i in range(1,n+1):
    s = s + pow(i,3)
print(s)    

