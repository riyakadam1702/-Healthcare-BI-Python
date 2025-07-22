#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Import required libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic


# In[24]:


# Reading theCSV File
df = pd.read_csv("train_data.csv")
df.head()


# In[15]:


# Checking Basic Info 
print("Shape", df.shape)
print("\nData Types\n", df.dtypes)
df.info()
df.describe(include = 'all')


# In[21]:


# Check for null values in all columns
print(df.isnull().sum())


# In[30]:


# Handling missing values

# Replacing the Null values in Bed Grade by the most common value (mode)
df['Bed Grade'].fillna(df['Bed Grade'].mode()[0], inplace=True)

# Replacing the City Code for the Patient with Group-Based Imputation 
df['City_Code_Patient'] = df.groupby('Hospital_code')['City_Code_Patient']\
                            .transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))
# Now check for missing values 
print(df.isnull().sum())


# In[22]:


# Heatmap for checking missing values
plt.figure(figsize=(12,6))
sns.heatmap(df.isnull(), cbar= False, cmap="YlOrRd")
plt.title("Missing Values Heatmap")
plt.show()


# In[23]:


# Checking for duplicate values 
print("Duplicate Rows", df.duplicated().sum()) 
# No Duplicate values 


# In[39]:


# Admission Deposite Vs Age Group -- Boxplot 
sns.boxplot(x='Age', y='Admission_Deposit', data=df)
plt.title('Admission Deposite Vs Age Group')
plt.xticks(rotation = 45)
plt.show()  


# # Insights 
# - For all age groups, most admission deposits seem to be between ₹4,000 and ₹6,000 cetering at ₹5000.
# - Significant outliers, meaning patients paid much more or less than ₹5000. 
# - No obvious trend observed (older = higher deposit), meaning age group may not significantly 
#   impact deposit amount.

# In[44]:


# Severity of Illness by Department -- Heatmap
pivot = df.pivot_table(index='Department', columns='Severity of Illness', aggfunc='size', fill_value=0)
sns.heatmap(pivot, annot=True, cmap='YlGnBu')
plt.title('Severity of Illness by Department')
plt.show()


# # Insights 
# - Gynecology department has the highest number of patients across all severity, especially Moderate.  
# - Surgery has an overall low count of patients expecially for Minor illness. 

# In[49]:


# Available Extra Rooms vs. Bed Grade -- Grouped Column Chart
sns.catplot(x='Bed Grade', y = 'Available Extra Rooms in Hospital', kind='bar', data=df, aspect=2)
plt.title("Available Extra Rooms vs. Bed Grade")
plt.show()


# # Insights 
# - Higher Grade beds are more in demand than lower Grades beds, resulting in more availability of Lower Grade beds 

# In[55]:


# Type of Admission vs. Stay Duration -- Stacked Bar Chart
stay_counts = df.groupby(['Type of Admission', 'Stay']).size().unstack().fillna(0)
stay_counts.plot(kind = 'bar', stacked=True)
plt.title('Type of Admission vs. Stay Duration')
plt.xlabel('Type of Admission')
plt.ylabel('Count of Patients')
plt.legend(title='Stay', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# # Insights
# - Trauma Admissions have the highest number of long-stay patients (taller bars overall).
# - Emergency also has large number of patients, but fewer long-stay patients as compared to Trauma.
# - Urget admission records least number of patients across all stays. 
# - 11-20 and 21-30 are the most common stays across all admission groups. 

# In[68]:


# Age Group vs. Stay Duration
age_stay = df.groupby(['Age', 'Stay']).size().unstack(fill_value=0)
age_stay.plot(kind='line',figsize=(12,6), marker='o')
plt.title('Stay Duration Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Patient Count')
plt.xticks(rotation=45)
plt.legend(title='Stay Duration', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# # Insights 
# - 31–40, 41–50, 51–60 — contribute the highest number of hospital stays overall, 11 to 30 days being most common. 
# - Very few patients across all age groups stay for more than 60 days.
# - Patients aged 0–10 and 11–20 have significantly lower patient counts across all stay durations.

# In[84]:


# Number of Visitor per Patient -- Histogram
plt.hist(df['Visitors with Patient'], bins=range(0, df['Visitors with Patient'].max()+2), color='mediumseagreen', align='left', rwidth=0.8)
plt.title('Number of Visitors per Patient')
plt.xlabel('Visitor Count')
plt.ylabel('Patient Frequency')
plt.show()


# # Insights 
# - Most patients have 1–3 visitors
# 

# In[85]:


# Bed Grade Vs Admission Deposit -- Violin Plot 
sns.violinplot(x='Bed Grade', y='Admission_Deposit', data=df, split=True, inner='quartile', palette='coolwarm')
plt.title('Deposit Distribution Across Bed Grades')
plt.show()


# # Insights 
# - Almost similar amounts deposited for all kinds of Bed Grades, indicating no dependancy of Admission Deposit on Bed grade. 
# - Long tails meaning there are higher deposits made from all bed grade patients. 

# In[89]:


import plotly.express as px
fig = px.treemap(df,
                 path=['Bed Grade', 'Ward_Type'],
                 values=df['Stay'].astype('category').cat.codes,
                 title='Stay Duration by Bed Grade and Ward Type')
fig.show()


# In[ ]:




