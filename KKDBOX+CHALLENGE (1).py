
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn


# In[2]:


# READ MEMBERS DATASET 


members = pd.read_csv("F:/KKBOX/members.csv", sep = ",")

# Sample submission zero

sample_submission_zero = pd.read_csv("F:/KKBOX/sample_submission_zero.csv", sep = ",")

# READ train dataset 

train  = pd.read_csv("F:/KKBOX/train.csv", sep = ",")
test = pd.read_csv("F:/KKBOX/sample_submission_zero.csv")


# In[3]:


print("Wymiar treningowego Zestawu danych:")
print("Wiersze: ", train.shape[0], "Kolumny: ", train.shape[1])


# In[4]:


pd.crosstab(train['is_churn'], columns = "Count") 


# In[5]:


# Wczytanie zestawów transakcji 

transactions = pd.read_csv("F:/KKBOX/transactions.csv", sep = ",")


# In[6]:


print("Liczba kolumn zestawu z transakcjami ", transactions.shape[1])
print("Liczba wierszy zestawu z transakcjami", transactions.shape[0])


# In[7]:


# Informacje o kolumnach zestawu treningowego 
# Dodanie mediany, odchylenia standardowego, min, max

# Create an transaction_aggregate table, 
# which include descriptive statistics about historical elements 
# of actual amount paid 



transaction_aggregate = transactions[['msno', 'actual_amount_paid']].groupby(['msno']).agg(['mean','median', 'min', 'max', 'count'])
transaction_aggregate.columns


# In[8]:


transaction_aggregate.columns  = transaction_aggregate.columns.droplevel()


# In[9]:


transaction_aggregate.columns


# In[10]:


transaction_aggregate['msno']  =  transaction_aggregate.index


# In[11]:


# Rename variables in transaction_aggregate dataset


transaction_aggregate = transaction_aggregate.rename(index = str, columns = {"max" : "trans_max", 
                                                     "count" : "trans_count", 
                                                     "median" : "trans_median", 
                                                     "max"    : "trans_max", 
                                                     "mean"   : "trans_mean"})


# In[12]:


transaction_aggregate.columns


# In[13]:


# Join 5 variables from transaction_aggregate dataset 

train = pd.merge(train, transaction_aggregate, how = 'left', on = 'msno')
test  =  pd.merge(test, transaction_aggregate, how = 'left', on = 'msno')


# In[14]:


train.shape


# In[15]:


train.columns


# In[16]:


# Get min and max transaction date, grouped by msno 

trans_date_agg = transactions[['msno', 'transaction_date']].groupby(['msno']).agg(['min', 'max'])


# In[17]:


trans_date_agg.columns = trans_date_agg.columns.droplevel()


# In[18]:



trans_date_agg.shape
#trans_date_agg.drop_duplicates

trans_date_agg['msno']   = trans_date_agg.index


# In[19]:


trans_date_agg = trans_date_agg.rename(index = str, columns = 
                         {"min" : "min_trans_date", 
                         "max"  : "max_trans_date"
                         })


# In[20]:


train = pd.merge(train, trans_date_agg,  how = 'left', on = 'msno')
test = pd.merge(test, trans_date_agg, how = 'left', on = 'msno')


# In[21]:


train.shape


# In[22]:


# Get differences between transaction dates
train['max_trans_date']  = pd.to_datetime(train['max_trans_date'], format = "%Y%m%d")
train['min_trans_date']  = pd.to_datetime(train['min_trans_date'], format = "%Y%m%d")
train['trans_date_diff']  =  train['max_trans_date'] - train['min_trans_date']
test['max_trans_date']  = pd.to_datetime(test['max_trans_date'], format = "%Y%m%d")
test['min_trans_date']  = pd.to_datetime(test['min_trans_date'], format = "%Y%m%d")
test['trans_date_diff']  =  test['max_trans_date'] - test['min_trans_date']


# In[23]:


from datetime import datetime, timedelta

train['trans_date_diff_num']  = train['trans_date_diff'] /  timedelta(days = 1)

test['trans_date_diff_num']  = test['trans_date_diff'] /  timedelta(days = 1)


# In[24]:


train['trans_date_diff_mon'] = train['trans_date_diff'] /  timedelta(days = 30)
test['trans_date_diff_mon'] = test['trans_date_diff'] /  timedelta(days = 30)


# In[ ]:


pd.DataFrame.to_csv(train, "F:/KKBOX/train_trans.csv", sep = ",")
pd.DataFrame.to_csv(test, "F:/KKBOX/test_trans.csv", sep = ",")



# In[ ]:


# User logs csv
# EEEEEND - wait 

user_logs = pd.read_csv("F:/KKBOX/user_logs.csv", usecols = ['msno'])


# In[ ]:


user_logs.shape


# In[ ]:


user_logs = pd.DataFrame(user_logs['msno'].value_counts().reset_index())
user_logs.columns = ['msno', 'logs_count']



train = pd.merge(train, user_logs, how = 'left', on = 'msno')
test  = pd.merge(test,  user_logs, how = 'left', on = 'msno')





# In[ ]:


train.shape


# In[ ]:





# In[ ]:


# Wczytanie all dataset 


user_logs = pd.read_csv("F:/KKBOX/user_logs.csv", sep = ",", nrows = 2000000)
user_logs.shape



# In[ ]:


user_logs.columns


# In[ ]:


user_logs.head


# In[ ]:


# Sample of user_logs  


uslog_try = pd.read_csv("F:/KKBOX/user_logs.csv", nrows = 100)


# In[ ]:


uslog_try.columns


# In[ ]:


uslog_try.head


# In[ ]:




