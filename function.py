#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
dice=[1,2,3,4,5]


# In[ ]:





# In[6]:


print(random.choice(dice))


# In[7]:


help(random)


# In[1]:


print(dir())


# In[1]:


import re


# In[12]:


s="ABCDE1234A"
r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l=re.findall(r,s)
print(l)

