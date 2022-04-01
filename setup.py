#!/usr/bin/env python
# coding: utf-8

# In[6]:


from setuptools import setup


# In[9]:


setup(
    name             = 'KRBday',
    version          = '1.0',
    description      = 'KR businessday',
    author           = 'Jeong Min Lee',
    author_email     = 'dcdc71581@gmail.com',
    url     = 'https://github.com/mtljm/KRBday.git',
    install_requires = ['bs4','requests','datetime' ],
    keywords         = ['KR','business day'],
    python_requires  = '>=3',
    zip_safe=False
)

