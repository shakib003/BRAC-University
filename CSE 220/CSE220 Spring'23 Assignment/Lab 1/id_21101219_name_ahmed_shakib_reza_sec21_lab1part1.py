# -*- coding: utf-8 -*-
"""ID: 21101219_Name: Ahmed Shakib Reza_Sec21_Lab1Part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzMEx25FrNeSpQFWMy8Si1_PZuWH-iF6

**Instructions to Follow (Failing to follow these will result mark penalties).**


1.   You can not use any built-in function except len()
2.   You can not use any other python collections except list (e.g: tuptle, dictionaries etc.)
3. If you need to initialize a new array using python list, you must mention the fixed size during initialization. There might be two approach. However, initializing new array in this lab is not mandatory.

  i. arr = [None] * 10 #Initializing an array length 10 with values None.

  ii. arr = [10, 20, 30, 40] #Initializing an array length 4 with the values.
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest

# Complete the functions defined in this cell

# Test 01: Shift Left k cell
def shift_left(source, k):
  for i in range(0,len(source)-k):
    source[i] = source[i+k]
    source[i+k] = 0
  return source



# Test 02: Rotate Left k cell
def rotate_left(source, k):
  # TO DO
  arr = [0]*k
  
  for i in range(0,k):
    arr[i] = source[i]
  #print(arr)
  idx = 0
  for j in range(0,len(source)-k):
    source[j] = source[j+k]
    source[j+k] = arr[idx]
    idx+=1
  return source



# Test 03: Shift Right k cell
def shift_right(source, k):
  # TO DO
  # Hint, You can write a function for right shift once and then use it
  for i in range(len(source)-1,0,-1):
    if i >= k:
      source[i] = source[i-k]
      source[i-k] = 0
  return source



# Test 04: Rotate Right k cell
def rotate_right(source, k):
  # TO DO
  # Hint, You can write a function for right rotate once and then use it
  arr = [0]*k
  idx = 0
  for i in range(k,len(source)):
    arr[idx] = source[i]
    idx+=1
  idx2 = len(arr)-1
  for i in range(len(source)-1,0,-1):
    if i >= k:
      source[i] = source[i-k]
      source[i-k] = arr[idx2]
      idx2-=1
  return source




# Test 05: Remove an element from an array
def remove(source, idx):
  for i in range(idx,len(source)-1):
    source[i] = source[i+1]
    source[i+1] = 0
  return source



# Test 06: Remove all occurrences of a particular element from an array
def remove_all(source, element):
  # TO DO
  idx = 0
  size = 0
  for i in source:
    if i != 0:
      size+=1
  temp = size
  while True:
    if idx == size:
      break
    if source[idx] == element:
      temp-=1
      for i in range(idx,temp):
        source[i] = source[i+1]
      source[temp] = 0
    else:
      idx+=1

  return source





source = [10,2,30,2,50,2,2,0,0]



# Test 07: Splitting an Array
def split_array(a):
  # TO DO

  for i in range(0,len(a)):
    sum1 = 0
    sum2 = 0
    if i != len(a)-1:
      for j in range(0,i+1):
        sum1 = sum1 + a[j]
      for k in range(i+1,len(a)):
        sum2 = sum2 + a[k]
      if sum1 == sum2:
        return True
    else:
      return False
    


# Test 08: Max Bunch Count
def max_bunch(a):
  # TO DO
  b = 0

  for i in range(0,len(a)):
    c = 0
    for j in range(i,len(a)):
      if a[i] == a[j]:
        c += 1
        if c>b:
          b = c
      else:
        c = 0
  return b

# This cell is the driver code
# Run this cell after completion of above function.
# You will see the status Accepted after completion if your code is correct.
# If your function is wrong you will see wrong[correction percentage]
# This is call unit testing if you are wondering the checking approach
# No need to write or change any code here

print("///  Test 01: Shift Left k cell  ///")
source = [10,20,30,40,50,60]
returned_value = shift_left(source, 3) # This should return [40, 50, 60, 0, 0, 0]
unittest.output_test(returned_value, [40, 50, 60, 0, 0, 0])


print("///  Test 02: Rotate Left k cell  ///")
source = [10,20,30,40,50,60]
returned_value = rotate_left(source, 3) # This should return [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, [40, 50, 60, 10, 20, 30])


print("///  Test 03: Shift Right k cell  ///")
source = [10,20,30,40,50,60]
returned_value = shift_right(source, 3) # This should return [0, 0, 0, 10, 20, 30]
unittest.output_test(returned_value, [0, 0, 0, 10, 20, 30])


print("///  Test 04: Rotate Right k cell  ///")
source = [10,20,30,40,50,60]
returned_value = rotate_right(source, 3) # This should return [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, [40, 50, 60, 10, 20, 30])


print("///  Test 05: Remove an element from an array  ///")
source = [10,20,30,40,50,0,0]
returned_value = remove(source, 2) # This should return [10, 20, 40, 50, 0, 0, 0]
unittest.output_test(returned_value, [10, 20, 40, 50, 0, 0, 0])


print("///  Test 06: Remove all occurrences of a particular element from an array  ///")
source = [10,2,30,2,50,2,2,0,0]
returned_value = remove_all(source, 2) # This should return [10, 30, 50, 0, 0, 0, 0, 0, 0]
unittest.output_test(returned_value, [10, 30, 50, 0, 0, 0, 0, 0, 0])


print("///  Test 07: Splitting an Array  ///")
test_1 = [1, 1, 1, 2, 1] # Here splitting is possible as summation of [1, 1, 1] = summation of [2,1]
returned_value = split_array(test_1) # This should return True
test_2 = [2, 1, 1, 2, 1] # Here splitting is not possible
returned_value = split_array(test_2) # This should return False
test_3 = [10, 3, 1, 2, 10] # Here splitting is possible as summation of [10, 3] = summation of [1,2,10]
returned_value = split_array(test_3) # This should return True
unittest.output_test(split_array(test_1), True)
unittest.output_test(split_array(test_2), False)
unittest.output_test(split_array(test_3), True)


print("///  Test 08: Max Bunch Count  ///")
returned_value = max_bunch([1, 2, 2, 3, 4, 4, 4]) # This should return 3
unittest.output_test(returned_value, 3)
returned_value = max_bunch([1, 1, 2, 2, 1, 1, 1, 1]) # This should return 4
unittest.output_test(returned_value, 4)