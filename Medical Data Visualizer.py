#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize cholesterol and glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Create 'cardio' chart
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Value counts for cardio=1
sns.countplot(x='variable', hue='value', data=pd.melt(df[df['cardio'] == 1],
                                                       value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active']),
              ax=axes[0]).set_title('Cardio = 1')

# Value counts for cardio=0
sns.countplot(x='variable', hue='value', data=pd.melt(df[df['cardio'] == 0],
                                                       value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active']),
              ax=axes[1]).set_title('Cardio = 0')

# Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# Create correlation matrix
corr_matrix = df.corr()

# Plot correlation matrix
mask = np.triu(corr_matrix)
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.1f', cmap='coolwarm', mask=mask, vmax=0.3, center=0, square=True, linewidths=.5)
plt.title('Correlation Matrix (Figure 2)')
plt.show()


# In[ ]:




