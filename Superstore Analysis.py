#!/usr/bin/env python
# coding: utf-8

# # Super Store Analysis
# 

# In[19]:


# import the necessary Library

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


# In[20]:


# load and read data file
s_store= pd.read_csv(r"C:\Users\preci\Downloads\Stores.csv") #copy the file path into the string
s_store


# In[21]:


# check the first five rows
s_store.head()


# In[22]:


# check data shape
s_store.shape


# In[23]:


# check data columns
s_store.columns


# In[24]:


# check data types
s_store.dtypes


# In[44]:


# change store ID data type to unique
s_store['Store ID '] = s_store['Store ID '].astype(int)


# In[45]:


# check data types
s_store.dtypes


# In[27]:


# check info about data
s_store.info()


# In[28]:


s_store.isnull().sum()


# In[29]:


# Do staticscal descriptive analysis of numerical values
s_store.describe().astype('int')


# In[31]:


# check for duplicate
s_store.duplicated().sum()


# In[69]:


grouped = s_store.groupby('Store ID ')['Store_Sales'].sum().sort_values(ascending = False)

print(grouped)


# In[70]:


# top 10 stores by revenue
grouped10 =grouped.head(10).sort_values(ascending = False)
grouped10


# In[71]:


# plot bar chart
g10 =grouped10.plot(kind = 'bar', figsize = (10, 5), title = 'Top 10 Store ID By Revenue', xlabel = 'Store ID', 
                        ylabel = 'Revenue', legend = False)

# annotate
g10.bar_label(g10.containers[0], label_type = 'edge')

#pad the spacing between the number and edge of the figure
g10.margins(y = 0.1)

# show the visual
plt.show()


# In[72]:


grouped1 = s_store.groupby('Store ID ')['Daily_Customer_Count'].sum().sort_values(ascending = False)


print(grouped1)


# In[73]:


# top 10 stores by Daiy Count of customers
grouped1_ =grouped1.head(10).sort_values(ascending = False)
grouped1_


# In[74]:


# plot bar chart
g11 =grouped1_.plot(kind = 'barh', figsize = (10, 5), title = 'Top 10 Store ID By Daily Count Of Customers', xlabel = 'Store ID', 
                        ylabel = 'Revenue', legend = False)

# annotate
g11.bar_label(g11.containers[0], label_type = 'edge')

#pad the spacing between the number and edge of the figure
g11.margins(y = 0.1)

# show the visual
plt.show()


# In[67]:


# top 5 Store ID by store Area using pie chart
top3_loc = s_store['Store ID '].groupby(s_store.Store_Area).sum().sort_values(ascending = False).head(5)
top3_loc


# In[68]:


# Visuzlize Top 5 location by price
explode= (0.1, 0, 0)
plt.pie(top3_loc, labels = top3_loc.index, autopct = '%1.1f', shadow = True, startangle= 140)
plt.title('Top 5 store area')
plt.show


# In[78]:


rr =s_store.sort_values(by='Items_Available')
rr


# In[79]:


# Correlatinon between Daily Customer Count and items Available

sns.lmplot(data= rr.sort_values(ascending = False).head(10), x= 'Daily_Customer_Count', y = 'Items_Available' , hue = 'Store ID ') 


# In[ ]:


# Correlatinon between price and furnished apartment

sns.regplot(data= s_store.sort_values(by='Items_Available') , x= 'Furnished', y = 'price')

