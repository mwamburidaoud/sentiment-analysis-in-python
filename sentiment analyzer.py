#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


Feedback1 = "This movie is good"
Feedback2 = "This movie is not good"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob1.sentiment)


# In[3]:


Feedback1 = "This movie is good"
Feedback1 = "This movie is awesome"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob1.sentiment)


# In[ ]:




