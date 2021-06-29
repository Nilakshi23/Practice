#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup=()


# In[2]:


type(tup)


# In[3]:


tup=(1,2,'str')


# In[4]:


print(tup)


# In[5]:


min(tup)


# In[6]:


len(tup)


# In[7]:


tup2=(1,2,3)


# In[8]:


cmp(tup,tup2)


# In[ ]:


#SET
# Set
#Sets are used to store multiple items in a single variable.

#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

#A set is a collection which is both unordered and unindexed.

#Sets are written with curly brackets.


# In[12]:


set1={'apple','banana'}


# In[13]:


type(set1)


# In[14]:


for x in set1:
    print(x)


# In[16]:


#to add items
set1.add('jello')


# In[18]:


print(set1)


# In[19]:


#TO ADD TWO SETS
set2={'hi','bye'}
set1.update(set2)


# In[20]:


set1


# In[21]:


#join two sets
set1.union(set2)


# In[ ]:


add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

