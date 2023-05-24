# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ojRsZ1IDvYAJjVvtUTy-ZQ0IEF8nbkxP
"""

#task 1

def dp(n):
    
  array = [1000000000]*(n+1)
  array[0] = 0
    
  for i in range(1,n+1):
    j = i
    while(j>0):
      temp = j%10
      array[i] = min(array[i],array[i-temp]+1)
      j = j//10
            
  print(array[n])


dp(25)