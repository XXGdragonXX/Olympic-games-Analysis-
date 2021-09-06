#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


athlete = pd.read_csv("C:/Users/MAHE/Desktop/athlete_events.csv")
regions = pd.read_csv('E:/noc_regions.csv')


# In[3]:


athlete.head()


# In[4]:


regions.head()


# In[5]:


athlete_df = athlete.merge(regions,how='left',on='NOC')


# In[6]:


athlete_df.head()


# In[7]:


athlete_df.shape


# In[8]:


athlete_df.rename(columns={'region':'Region'},inplace=True)
athlete_df.rename(columns={'notes':'Notes'},inplace=True)


# In[9]:


athlete_df.head()


# In[10]:


athlete_df.isnull().sum()


# In[11]:


athlete_df.describe()


# In[12]:


athlete_df.columns[athlete_df.isnull().any()]


# In[13]:


athlete_df.columns[athlete_df.isnull().any()].tolist() 


# In[14]:


athlete_df.query('Team == "India"').head()


# In[15]:


top_10_countries= athlete_df.Team.value_counts().sort_values(ascending =False).head(10)
top_10_countries


# In[16]:


plt.figure(figsize=(12,6))
plt.title=('Top 10 countries with most participants')
sns.barplot(x=top_10_countries.index,y=top_10_countries,palette='tab10')


# In[17]:


plt.figure(figsize=(12,6))
plt.title=('Age Distribution')
plt.xlabel("Ages")
plt.ylabel("Number of Athletes")
plt.hist(athlete_df.Age,bins=np.arange(10,60,2),color='Red',edgecolor='white');
plt.show()


# In[18]:


winter_sports = athlete_df[athlete_df.Season=='Winter'].Sport.unique()


# In[19]:


winter_sports


# In[20]:


summer_sports = athlete_df[athlete_df.Season=='Summer'].Sport.unique()
summer_sports


# In[21]:


gender_count = athlete_df.Sex.value_counts()
gender_count


# In[22]:


plt.figure(figsize=(12,6))
plt.title=("Gender Distribution")
sns.barplot(x=gender_count.index,y=gender_count)


# In[23]:


medal=athlete_df.Medal.value_counts()
medal


# In[24]:


plt.figure(figsize=(12,6))
plt.title=("Medal distribution")
sns.barplot(x=medal.index,y=medal)


# In[25]:


#female participants
Women_participants=athlete_df[(athlete_df.Sex=='F')&(athlete_df.Season=='Summer')][['Sex','Year']]
Women_participants=Women_participants.groupby('Year').count().reset_index()


Women_participants.head(10)


# In[26]:


women_olympics = athlete_df[(athlete_df.Sex=='F')&(athlete_df.Season=='Summer')]


# In[27]:


plt.figure(figsize=(20,10))
sns.set(style="darkgrid")
sns.countplot(x='Year',data=women_olympics,palette='Spectral')
#plt.title('Women_Participation')


# In[28]:


#gold medal athletes
gold_medal=athlete_df[(athlete_df.Medal=='Gold')&(athlete_df.Season=='Summer')]


# In[29]:


gold_medal.head()


# In[30]:


gold_medal=gold_medal[np.isfinite(gold_medal['Age'])]


# In[31]:


gold_medal.head()


# In[32]:


#gold medals from each country
TGM = gold_medal.Region.value_counts().head(10)


# In[33]:


TGM


# In[34]:


plt.figure(figsize=(20,10))
#plt.title('Gold medals per country')
sns.barplot(x=TGM.index,y=TGM,palette='Set2');


# In[36]:


gold_medal[gold_medal.Region=='India'].head(10)


# In[43]:


gold_medal[gold_medal.Region=='India'].value_counts


# In[68]:


#Rio olympics
max=athlete_df.Year.max()


# In[69]:


print(max)


# In[70]:


rio_2016=athlete_df[(athlete_df.Year==max)&(athlete_df.Medal=='Gold')].Team
rio_2016.value_counts().head(10)


# In[75]:


plt.figure(figsize=(20,10))
sns.barplot(x=rio_2016.value_counts().head(10),y=rio_2016.value_counts().head(10).index)


# In[81]:


plt.figure(figsize=(20,10))
sns.scatterplot(x=rio_2016.value_counts().head(20),y=rio_2016.value_counts().head(20).index)


# In[ ]:




