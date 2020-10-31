#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


df=pd.read_csv('Birth_Death.csv')
print(df)


# In[45]:


df.head()


# In[46]:


df.shape


# In[47]:


df.describe()


# In[48]:


df.columns


# In[49]:


df.dtypes


# In[50]:


plt.xlabel('Year')
plt.plot(df.Period.value_counts().sort_index())


# In[51]:


sns.barplot(df.Period.sort_index(), df.Count.value_counts().sort_index())


# In[52]:


sns.heatmap(df.corr(), annot=True)


# In[ ]:




