#!/usr/bin/env python
# coding: utf-8

# # Segmenting and Clustering Neighborhoods in Toronto | Part-2

# In[1]:


get_ipython().system('pip install geocoder')


# In[2]:


import pandas as pd
import numpy as np
import geocoder
print("Imported!")


# In[3]:


df = pd.read_csv('toronto.csv')
df.head()


# In[4]:


print(df.shape)
df.describe()


# In[5]:


def get_latilong(postal_code):
    lati_long_coords = None
    while(lati_long_coords is None):
        g = geocoder.arcgis('{}, Toronto, Ontario'.format(postal_code))
        lati_long_coords = g.latlng
    return lati_long_coords
    
get_latilong('M4G')


# In[6]:


# Retrieving Postal Code Co-ordinates
postal_codes = df['Postalcode']    
coords = [ get_latilong(postal_code) for postal_code in postal_codes.tolist() ]


# In[7]:


# Adding Columns Latitude & Longitude
df_coords = pd.DataFrame(coords, columns=['Latitude', 'Longitude'])
df['Latitude'] = df_coords['Latitude']
df['Longitude'] = df_coords['Longitude']


# In[8]:


df[df.Postalcode == 'M5G']


# In[9]:


df.head(15)


# In[10]:


df.to_csv('toronto_part2.csv',index=False)


# In[ ]:




