#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
def intro(self):
    print("My name is",self.name)
    print("My age is",self.age)
    return name,age
        


# In[6]:





# In[16]:


h=Human("Nilax",25)


# In[17]:


h2=Human("Lol",59)


# In[33]:


h.intro()


# In[19]:


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)


# In[21]:


#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self,color,wheels):
        self.color=color
        self.wheels=wheels
        
class Bus(Vehicle):
   pass


# In[22]:


sbus=Bus("red",6)


# In[24]:


print(sbus.color)


# In[25]:


v1=Vehicle("yellow",4)


# In[26]:


print(v1.color)


# In[27]:


#Create a Bus class that inherits from the Vehicle class. 
#Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# In[ ]:





# In[28]:


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


# In[29]:


#Define property that should have the same value for every class instance
 #Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

#Use the following code for this exercis  
class Vehicle:
   color='white'
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

class Bus(Vehicle):
   pass

class Car(Vehicle):
   pass


# In[30]:


s_bus=Bus('t',12,34)


# In[31]:


s_bus.color


# In[ ]:





# In[57]:


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def seatingcap(self,capacity):
        return f"The seating capacity is {capacity} students"


# In[59]:


class Eachstudent(Student):
    def seatingcap(self, capacity=50):
        return super().seatingcap(capacity=50)
e1 = Eachstudent("School Volvo",12)
print(e1.seatingcap())


# In[66]:


#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
#If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
#So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
#You need to override the fare() method of a Vehicle class in Bus class.

#Use the following code for your parent Vehicle class. 
#We need to access the parent class from inside a method of a child class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
      def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# In[67]:


# Determine which class a given Bus object belongs to (Check type of an object)

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)


# In[74]:


type(School_bus)


# In[ ]:


#Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
   def __init__(self, name, mileage, capacity):
       self.name = name
       self.mileage = mileage
       self.capacity = capacity

class Bus(Vehicle):
   pass

School_bus = Bus("School Volvo", 12, 50)


# In[75]:


#Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)


# In[76]:


print(isinstance(School_bus, Vehicle))


# In[ ]:




