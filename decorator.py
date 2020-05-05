#!/usr/bin/env python
# coding: utf-8

# In[7]:


def deco_concat(func):
    def new_func(num1,num2):
        if type(num1)==type(num2):
           return func(num1,num2)
        else:
            return func(str(num1),str(num2))
    return new_func


@deco_concat
def concat(num1,num2):
    return num1+num2


result =concat(10,20)
print(result)

result =concat("java","python")
print(result)

result =concat("java",10)
print(result)

