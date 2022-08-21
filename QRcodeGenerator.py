#!/usr/bin/env python
# coding: utf-8

# In[12]:


pip install pyqrcode


# In[10]:


pip install pypng


# In[15]:


# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://github.com/AbdulNasir-NuZ"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "nasirGitqr.svg"
url.svg("nasirGitqr.svg", scale = 8)

# Create and save the png file naming "nasirGitqr.png"
url.png('nasirGitqr.png', scale = 6)


# In[ ]:




