# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:42:23 2019

@author: Admin
"""

import numpy as np
a=np.array([[1,4,2,3],
[3,6,7,5],[8,5,9,2],[2,3,6,7]])

print(a)
sum=0
s=0
for i in range(len(a)):
    for j in range(len(a[0])):
        if i+j==len(a)-1:
            sum+=a[i][j]
            
        elif i==j:
            s+=a[i][j]
        else:
            pass
        
        
            
print(s)
print(sum)
diff=abs(sum-s)
print(diff)