#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import datetime
from sklearn.metrics.pairwise import haversine_distances
from math import radians


# In[2]:


df = pd.read_csv('Car_Fair.csv')
df.head()


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


df.pickup_datetime = pd.to_datetime(df.pickup_datetime) - datetime.timedelta(hours=4)


# In[6]:


df.head()


# In[7]:


df['day'] = df.pickup_datetime.dt.day
df['month'] = df.pickup_datetime.dt.month
df['year'] = df.pickup_datetime.dt.year
df['hour'] = df.pickup_datetime.dt.hour
df['minute'] = df.pickup_datetime.dt.minute
df.drop('pickup_datetime', axis=1, inplace=True)


# In[8]:


df.head()


# In[9]:


df.columns


# In[10]:


df.dtypes


# In[12]:


def findDist(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude):
    pickup_long_rad = radians(pickup_longitude)
    pickup_lat_rad = radians(pickup_latitude)
    drop_long_rad = radians(dropoff_longitude)
    drop_lat_rad = radians(dropoff_latitude)
    dist = haversine_distances([[pickup_lat_rad,pickup_long_rad],[drop_lat_rad,drop_long_rad]])
    return dist * 6371   


# In[13]:


# Creating Distance column
rad = map(findDist, df.pickup_longitude,df.pickup_latitude,df.dropoff_longitude,df.dropoff_latitude)

distmat = list(rad)

distance = []
for i in distmat:
    distance.append(i[0][1])

df['distance'] = distance


# In[14]:


df.head()


# In[15]:


dist_data = df.drop(['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'day', 'month', 'year', 'hour', 'minute', 'passenger_count'], axis=1)


# In[16]:


dist_data.head()


# In[22]:


sns.barplot(df.day.sort_index(), df.passenger_count.value_counts().sort_index())


# In[23]:


plt.plot(df.day.value_counts().sort_index())


# In[ ]:




