#!/usr/bin/env python
# coding: utf-8

# # Assignment 1:
# 1. Sum of n numbers with help of while loop

# In[3]:


n = int(input())
sum = 0
i =1
while(i<=n):
    sum = sum + i
    i = i +1
    print("sum of the number", sum)


# 2. Check a given inter whether its prime or not .

# In[3]:


num = int(input("Enter a number:"))

if num>9:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not prime number")
            break
else:
    print(num,"is prime number")


# In[ ]:




