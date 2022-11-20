#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style


# In[2]:


time_data = {'facebook':120, 'youtube':90, 'instagram':40, 'snapchat':28}
social_media = list(time_data.keys())
time_spend = list(time_data.values())


# In[3]:


style.use('ggplot')
plt.figure(figsize=(5,5))
color = ['royalblue', 'red', 'purple', 'yellow']
plt.bar(social_media, time_spend, color=color, width=0.5)
plt.xlabel('Social Media')
plt.ylabel('Time in Minutes')
plt.title('Average time spend on social media')


# In[4]:


fb = (120, 90, 110, 100, 95)
yt = (80, 90, 75, 85, 95)
ig = (50, 40, 55, 35, 45)
sc = (20, 30, 35, 25, 28)


# In[5]:


xpos = np.arange(len(fb))
xpos


# In[6]:


style.use('ggplot')
plt.figure(figsize=(10,7))
barWidth = 0.2
plt.bar(xpos, fb, color='royalblue', width = barWidth, label='FB')
plt.bar(xpos+0.2, yt, color='red', width = barWidth, label='YT')
plt.bar(xpos+0.4, ig, color='purple', width = barWidth, label='IG')
plt.bar(xpos+0.6, sc, color='yellow', width = barWidth, label='SC')
plt.xticks(xpos+0.3, ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
plt.xlabel('Day')
plt.ylabel('Time spend in minutes')
plt.title('Time spend on social media')
plt.legend()


# In[7]:


fb = (120, 90, 110, 100, 95)
yt = (80, 90, 75, 85, 95)
ig = (50, 40, 55, 35, 45)
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
xpos = np.arange(len(x))
barWidth = 0.4
plt.figure(figsize=(10,7))
plt.bar(xpos, fb, color='royalblue', width= barWidth, label='FB')
plt.bar(xpos, yt, bottom=fb, color='red', width= barWidth, label='YT')
plt.bar(xpos, ig, bottom=yt, color='purple', width= barWidth, label='IG')
plt.xlabel('Day')
plt.ylabel('Time spend in minutes')
plt.title('Time spend on socia media')
plt.xticks(xpos, x)
plt.legend()


# In[9]:


import os
os.chdir(r'E:\The AI & DS Channel\35_Bar chart\working file\data')


# In[10]:


car_sales = pd.read_csv('Car_sales.csv')
car_sales.head()


# In[11]:


manufacturer = car_sales['Manufacturer']
sales = car_sales['Sales_in_thousands']


# In[12]:


fig = plt.figure(figsize=(15,10))
plt.bar(manufacturer, sales)
plt.xlabel('Car Manufacturer')
plt.ylabel('Sale in 1000s')
plt.title('Car Sales')
plt.show()


# In[13]:


fig = plt.figure(figsize=(15,10))
plt.barh(manufacturer, sales, color='purple')
plt.xlabel('Car Manufacturer')
plt.ylabel('Sale in 1000s')
plt.title('Car Sales')
plt.show()


# In[28]:


toyota_df = car_sales.groupby('Manufacturer').get_group('Toyota')
toyota_df


# In[29]:


model = toyota_df['Model']
fuel_capacity = toyota_df['Fuel_capacity']
fuel_efficiency = toyota_df['Fuel_efficiency']


# In[30]:


fig = plt.figure(figsize=(15,10))
plt.barh(model, fuel_capacity, color='blue', height=0.5, label='Fuel Capacity')
plt.barh(model, fuel_efficiency, left=fuel_capacity, color='red', height=0.5, label='Fuel Capacity')
plt.ylabel('Car Model')
plt.xlabel('Fuel Capacity and Fuel Efficiency')
plt.title('Fuel capacity & fuel efficiency of various car models')
plt.legend()
plt.show()


# In[ ]:




