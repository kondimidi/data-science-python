# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import pandas as pd


string = 'workout summer good free holiday time time hot'
split_string = string.split(' ')

s = pd.Series(split_string)

# %%
s.str.contains(r'[0-9]')
s.str.contains(r'[a-z]')

s.str.contains(r'[rg]')
