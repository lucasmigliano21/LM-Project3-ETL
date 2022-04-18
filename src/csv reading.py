#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from src import functions as fn
import pandas as pd


# In[ ]:


results=pd.read_csv('./data/results_teams.csv')


# In[ ]:


fn.column_cleaning(results)


# In[ ]:


results = fn.filter(results)


# In[ ]:


results = fn.winner(results)


# In[ ]:


results_csv=fn.copy(results)


# In[ ]:


results_csv.to_csv('./data/results.csv', index=False)

