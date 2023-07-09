#!/usr/bin/env python
# coding: utf-8

# In[5]:


#adding two numbers
num1 = 20
num2 = 40
sum = num1 + num2
print('Sum of', num1, 'and', num2, 'is', sum)


# In[11]:


#maximum of two numbers in python
a = 20
b = 40
maximum = max(a,b)
print(maximum)


# In[12]:


a = 20
b = 40
print(a if a >= b else b)


# In[14]:


def maximum (a, b):
    if a >= b:
        return a
    else:
        return b
a = 20
b = 40
print(maximum(a, b))


# In[4]:


#python program for factorial of a number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
num = 5 
print("Factorial of", num,"is", factorial(num))


#  

# In[3]:


#python program for simple interset
p = int(input("Enter principal : "))
t = int(input("Enter time : "))
r = int(input("Enter rate : "))
si =(p*t*r)/100
print("simple Interset is : ",si)


# In[4]:


#compound interset
p = int(input("Enter principal : "))
t = int(input("Enter time : "))
r = int(input("Enter rate : "))
amount = p*(pow((1+r/100),t))
ci = amount-p
print("compound interset is:",ci)


# In[5]:


#python program for program to find area of circle
import math
radius = float(input("Enter thr radius of the circle : "))
area = math.pi * radius * radius
print("Area of the circle is : {0}".format(area))


# In[3]:


#python program to print all prime numbers in an interval
lower = int(input("enter lower limit here (>1) : "))
upper = int(input("enter the upper limit here: "))
for i in range  (lower,upper+1):
    if i > 1:
        for num in range (2,i):
            if i%num==0:
                break
                  
            else: 
                print (i)


# In[3]:


#python program to check whether a number is prime or not
num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# In[14]:


#python program for n-th Fibonacci number
n1 = 0
n2 = 1
count = 2
if n < 0:
    print("Enter only positive values")
elif n == 1:
    print(n1)
else:
    print(n2)
    print(n2)
    while count < n:
        n3 = n1 +n 2
        print(n3)
        count+ =1
        n1 = n2
        n2 = n3


# In[13]:


#python program for sum of squares of first n natural numbers
def squaresum(n):
 
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
    return sm
n = 4
print(squaresum(n))


# In[ ]:




