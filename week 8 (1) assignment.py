#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# Q=1 Create a pandas series that contains the following data : 4,8,15,16,23, and 42. Then ,print the series.

# In[7]:


d=pd.Series([4,8,15,16,23,42])


# In[8]:


d


# Q-2 Create a variable of list type containing 10 elements in it ,and apply pandas .series function on the variable print it.

# In[12]:


d=list(('a','b','c','d','e','f','g','h','i','h'))


# In[13]:


d


# Q-3 Create a pandas DataFrame that contains the following data:
# 

# In[4]:


data={"Name":["Alice","Bob","Claire"],
      "Age":[25,30,27],
      "Gender":["Female","Male","Female"]}


# In[5]:


df=pd.DataFrame(data)


# In[6]:


df


# Q-4 What is dataframe in pandas and how is it different from pandas .series? Explian with an example.

#  Ans=4 A data frame is a two dimentional data structure ,i.e., data is aligned in a tabular fashion in rows and columns . we can perform basic operations on rows/columns like selecting , deleting ,adding and renaming.
#  
#  Difference :-
#               As noted in the table , a pandas series is a 1D array of data, but a single- column dataframe is a 2D table with one column.The main difference b/w them is for a single- column dataframe , an index can be optional , but a series has to have an index defined.

# In[7]:


data=["neha","muskan","nancy","sarita"]
df=pd.Series(data)


# In[8]:


df


# Q-5 What are some  common functions you can use to manipulate data in a pandas dataframe ? can you give an examplpe of when you might use one of these function?

# Ans-5 some data manipulation in python 
# 1. Installing pandas
# 2. creating dataframe
# 3. Adding data in dataframe using append function 
# 4. Getting shape and information of the data
# 5. Dropping columns from data

# In[9]:


import pandas as pd
data={"Name":["Alice","Bob","Claire"],
      "Age":[25,30,27],
      "Gender":["Female","Male","Female"]}
df=pd.DataFrame(data)


# In[10]:


df


# Q-6 Which of the following is mutable in nature series , dataframe,panel?

# Ans-6 Dataframe are both value and size mutable ,A series by contrast , is only value mutable , not size mutable . In panel data and size are mutable. 

# Q-7 Create a dataframe using multiple series . Explain with an example.

# In[19]:


import pandas as pd
name_series=pd.Series(["neha","muskan","nancy","sarita"])
age_series=pd.Series([20,16,17,18])

frame={"name":name_series,
       "age":age_series}
# creating dataframe 
df=pd.DataFrame(frame)
address=pd.Series(["Bareilly","Muradabad","Nawabganj","Ram Nagar"])
frame['address']=pd.Series(address)
print(frame)


# In[ ]:




