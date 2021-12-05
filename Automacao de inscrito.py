#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pyscreenshot 
from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get ("https://www.youtube.com/c/D1JornadasDigitais") 
navegador.get("https://www.youtube.com/c/D1JornadasDigitais/about")
image = pyscreenshot.grab () 
image.show() 
image.save("Numerodeinscrito.png") 
screenshot = navegador.save_screenshot('Numerodeinscrito.png')


# In[ ]:





# In[ ]:





# In[ ]:




