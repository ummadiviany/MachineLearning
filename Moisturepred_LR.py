#!/usr/bin/env python
# coding: utf-8

# In[155]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[156]:


from sklearn import linear_model
#from sklearn.linear_model import LinearRegression
url = 'https://thingspeak.com/channels/539123/field/4.csv'
#df = pd.read_csv('C:/Users/lenovo/Downloads/4.csv')
df=pd.read_csv(url)
df.columns = ['created_at','entry_id', 'field4']
#plt.plot(df)
#plt.show()
df.head()


# In[157]:


sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.lmplot('entry_id','field4', data=df)
plt.ylabel('Moisture')
plt.xlabel('entry_id')
df['x']=df['entry_id']
df['y']=df['field4']
df.head()
df.describe()


# In[158]:


xlen=len(df.x)
ylen=len(df.y)


# In[160]:


linear = linear_model.LinearRegression()
trainx = np.asarray(df.x[10:xlen]).reshape(-1, 1)
trainy = np.asarray(df.y[10:ylen]).reshape(-1, 1)
#len(df.y)
testx = np.asarray(df.x[:10]).reshape(-1, 1)
testy = np.asarray(df.y[:10]).reshape(-1, 1)
linear.fit(trainx, trainy)
linear.score(trainx, trainy)
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print('R² Value: \n', linear.score(trainx, trainy))
predicted = linear.predict(testx)


# In[159]:


print(predicted)
plt.plot(predicted)
plt.show()


# In[166]:


print(predicted)
out=np.reshape(predicted,(1,-1))
out.to_clipboard()


# In[ ]:





# In[ ]:




