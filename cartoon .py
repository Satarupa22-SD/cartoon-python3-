#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


pip install numpy


# In[3]:


import cv2


# In[4]:


import numpy as np
from tkinter.filedialog import *


# In[5]:


photo = askopenfilename()
img = cv2.imread(photo)


# In[6]:


grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


# In[7]:


#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)


# In[8]:


cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)


# In[ ]:


#save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




