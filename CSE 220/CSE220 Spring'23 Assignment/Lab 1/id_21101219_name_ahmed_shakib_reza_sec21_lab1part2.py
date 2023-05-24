# -*- coding: utf-8 -*-
"""ID: 21101219_Name: Ahmed Shakib Reza_Sec21_Lab1Part2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1FIhBJcUHDCkwjIP6-oM3UvmatnIna2
"""

def mean(arr):
  sum = 0
  n = 0
  for i in arr:
    sum = sum + i
    n += 1
  mean = sum/n
  return mean

def Standard_Deviation(arr,mean):
  n = len(arr)
  sd_sum = 0
  for i in arr:
    temp = (i-mean)**2
    sd_sum = sd_sum + temp
  sd = (sd_sum/(n-1))**0.5
  return sd

def new_array(arr,sd):
  arr2 = [0]*len(arr)
  idx = 0
  for i in arr:
    if (i-mean)/sd >= 1.5:
      arr2[idx] = i
      idx+=1
    if (mean-i)/sd >= 1.5:
      arr2[idx] = i
      idx+=1
  count = 0
  for elem in arr2:
    if elem != 0:
      count += 1
  if count != 0:
    arr3 = [0] * count
    for i in range(0,len(arr3)):
      arr3[i] = arr2[i] 
    return arr3
  else:
    return None

arr = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
mean = mean(arr)
sd = Standard_Deviation(arr,mean)
new = new_array(arr,sd)

print(f'The mean of the numbers is: {mean}')
print(f'The standard deviation is: {"%.2f"%sd}')
print(f'New array: {new}')