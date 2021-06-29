#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lists
l1=[1,2,3,4,5,6]
print(l1)


# In[2]:


l1[:]


# In[3]:


l1[0:]


# In[4]:


l1[1:]


# In[5]:


l1[1:4]


# In[6]:


l1[0:7:2]


# In[7]:


l1[::-1]


# In[8]:


l1[:-1]


# In[9]:


#to update the element
l1[1]=10


# In[10]:


l1


# In[11]:


print(l1)


# In[12]:


#repetition
l1*2


# In[13]:


print(l1)


# In[14]:


l2=[5,6,7,8,9,10]
l1+l2


# In[17]:


#Iteration
for i in l1:
    print(i)


# In[18]:


#len
print(len(l1))


# In[19]:


#adding elements to list:-
list_name.append(value)
list_name.insert(index,value)
l=[]
n=int(input("enter the elements"))
for i in range(0,n):
    l.append(input("Enter the item:"))
print(l)


# In[22]:


l=[]
n=int(input("enter the range"))
for i in range(0,n):
    
    l.append(int(input("enter elements")))
print(l)


# In[23]:


print(l)


# In[24]:


l.append(10)


# In[25]:


print(l)


# In[26]:


l.append(2)


# In[27]:


l.insert(2,49)


# In[28]:


print(l)


# In[29]:


l.remove(3)


# In[30]:


print(l)


# In[31]:


l.remove(2)


# In[32]:


print(l)


# In[33]:


del l[2]


# In[34]:


l


# In[35]:


l.pop(3)


# In[36]:


l


# In[ ]:


#To remove element by using INDEX use :-
del list_name[index position]
list_name.pop(index position)
#To remove element using value of list:-
list_name.remove(value)


# In[37]:


len(l)


# In[38]:


max(l)


# In[39]:


min(l)


# In[40]:


count(l)


# In[42]:


#to remove duplicate elements from list
list1 = [1,2,2,3,55,98,65,65,13,29] 
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


# In[45]:


#sum of elements in list
list1=[2,3,4,5,6]
for i in list1:
    sum+=i
print(sum)


# In[46]:


list1


# In[51]:


list2 =[2,4,6,8,9]
for i in list1:
    for n in list2:
        if i==n:
          print("the common element is",n)


# In[52]:


#LIST METHODS
L1=['ABC','xyz',1,2,3,4,'l',1,2,3]
#to count the no. of elements repeated
L1.count(2)


# In[53]:


#to extend list
l2=[1,2,3,4,45]
l1.extend(l2)


# In[54]:


l2


# In[55]:


print(l1)


# In[56]:


l1


# In[57]:


l1.reverse()


# In[58]:


l1


# In[59]:


l1.sort()


# In[60]:


l1


# In[61]:


#cONVERT LIST TO TUPLE
R=tuple(L1)


# In[62]:


R


# In[1]:


n=input("This is a sentence")
wordlist=n.split()
print(wordlist)


# In[2]:


import numpy as np


# In[5]:


a=np.array([10,20,30],[50,60,70])


# In[7]:


m=np.array([[10,20,30],[40,50],[60,70,80,90]])


# In[8]:


m


# In[9]:


m.shape


# In[10]:


m.ndim


# In[11]:


m.size


# In[16]:


m=np.arange(1,10,1).reshape(3,3)


# In[17]:


m


# In[20]:


for i in np.nditer(m[::]):
    print(i)


# In[ ]:




