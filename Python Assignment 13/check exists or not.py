# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:29:53 2021

@author: SUBHAM
"""

import os
if os.path.exists("file3.txt"):
  os.remove("file3.txt")
else:
  print("The file does not exist")

