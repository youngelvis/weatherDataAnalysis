#!/usr/bin/env python
# coding: utf-8

# The weather dataset

# In[1]:


import pandas as pd


# In[4]:


data = pd.read_csv('Documents/WeatherData.csv')


# # .head()

# It shows the first N rows in the data (by default, N=5

# In[5]:


data.head()


# # .shape()

#  It shows the total no. of rows and no. of columns of the dataframe

# In[7]:


data.shape


# # .index()

# This attribute provides the index of the dataframe

# In[8]:


data.index


# # .columns

# it shows the data-type of each column

# In[9]:


data.columns


# # .dtypes 
# 
# It shows the data-type of each column

# In[10]:


data.dtypes


# # .unique()
# 
# In a column, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe.

# In[12]:


data['Weather'].unique()


# # .nunique() 
# 
# It shows the total no. of unique values in each column. It can be applied on a single column as well as on the whole dataframe.

# In[13]:


data.nunique()


# # .count
# 
# it shows the total no. of non- null balues in each column. it can be applied on a single column as well as on whole dataframe

# In[15]:


data.count()


# # .value_counts
# 
# in a column, it shows all the unique values with their count. it can be applied on single column only.

# In[16]:


data['Weather'].value_counts()


# # .info()
# 
# provides basic information about the dataframe.

# In[17]:


data.info()


# # Q. 1)  Find all the unique 'Wind Speed' values in the data.

# In[18]:


data.head(2)


# In[19]:


data['Wind Speed_km/h'].nunique()


# In[20]:


data['Wind Speed_km/h'].unique()


# # Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[21]:


data.head(2)


# In[22]:


# value_count()

data.Weather.value_counts()


# In[26]:


# filtering

data.head(2)


# In[28]:


# filtering
data[data.Weather == 'Clear']


# In[30]:


#groupby()

data.groupby('Weather').get_group('Clear')


# # Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[34]:


data.head(2)
data[data['Wind Speed_km/h'] == 4]


# In[ ]:




